def render_text(self, block: str, block_type: str, y: int) -> int:
    """

    :param self: MarkdownRenderer
    :param str block: string of text
    :param str block_type: type of the text (e.g. headers, ordered/unordered lists, blockquotes, code etc)
    :param int y:  y-coordinate to start rendering on
    :returns: int - y-coordinate after rendering is finished
    """

    # if y == self.y - self.pixel_first_showable and block_type in ("h1", "h2", "h3"):
    #     y += self.gap_paragraph

    H1_OFFSET = 3
    H2_OFFSET = -7
    H3_OFFSET = -16

    start_of_line_x = self.x
    if block_type == "blockquote":
        start_of_line_x += self.indentation_quote
        quote_y_start = y

    x = start_of_line_x

    # Cleanup and stripping
    block = block.replace("\n", " ").strip(" ")
    if block[:3] == "<p>":
        block = block[3:]
    if block[-4:] == "</p>":
        block = block[:-4]

    code_flag = False
    bold_flag = False
    italic_flag = False
    position = None

    if block_type == "h1":
        y -= H1_OFFSET
    elif block_type == "h2":
        y -= H2_OFFSET
    elif block_type == "h3":
        y -= H3_OFFSET

    for word in block.split(" "):

        # _________ PREPARATION _________ #
        # inline code, bold and italic formatting
        (
            word,
            position,
            code_flag,
            bold_flag,
            italic_flag,
        ) = self.inline_formatting_preparation(
            word, position, code_flag, bold_flag, italic_flag
        )

        # _________ TEXT BLITTING _________ #
        # create surface to get width of the word to identify necessary linebreaks
        word = word + " "
        word = word.replace("&gt;", ">").replace("&lt;", "<")
        if code_flag:
            if position == "first" or position == "single":
                x += self.code_padding
            surface = self.get_surface(word, "code", bold_flag, italic_flag)
        else:
            surface = self.get_surface(word, block_type, bold_flag, italic_flag)

        text_height = surface.get_height()  # update for next line

        if x + surface.get_width() >= self.w:  # new line necessary
            y = y + self.gap_paragraph
            if block_type in ["h1", "h2", "h3"]:
                y += self.gap_paragraph
            x = start_of_line_x

        if self.is_visible(y) and self.is_visible(y + text_height):
            if block_type == "blockquote":  # draw quote-rectangle in front of text
                self.draw_quote_rect(
                    y, y + self.get_surface(word, "blockquote").get_height()
                )

            self.draw_code_background(code_flag, word, x, y, position)
            self.screen.blit(surface, (x, y))

        # Update x for the next word
        x = x + surface.get_width()
        if code_flag and position in ("single", "last"):
            x -= self.code_padding  # reduce empty space by padding.

        # _________ FORMATTING RESET FOR NEXT WORD _________ #
        bold_flag = False if bold_flag and position == "last" else bold_flag
        code_flag = (
            False
            if code_flag and (position == "last" or position == "single")
            else code_flag
        )
        italic_flag = False if italic_flag and position == "last" else italic_flag
        position = "Middle" if position == "first" else position

    if block_type in {"h1", "h2", "h3"}:
        if block_type == "h1":
            y += H1_OFFSET
        elif block_type == "h2":
            y += H2_OFFSET
        elif block_type == "h3":
            y += H3_OFFSET
        y += self.gap_paragraph

    return y
