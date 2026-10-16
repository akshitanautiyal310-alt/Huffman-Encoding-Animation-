from manim import *

class HuffmanAnimation(Scene):
    def make_node(self, label, pos, width=1.45):
        box = RoundedRectangle(
            corner_radius=0.12,
            width=width,
            height=0.72
        ).move_to(pos)
        text = Text(label, font_size=24).move_to(box.get_center())
        return VGroup(box, text)

    def connect(self, a, b):
        return Line(a.get_bottom(), b.get_top(), buff=0.08)

    def construct(self):
        title = Text("Huffman Encoding: Greedy Construction", font_size=34)
        title.to_edge(UP)
        self.play(Write(title))

        values = [("A", 5), ("B", 9), ("C", 12), ("D", 13), ("E", 16)]
        nodes = []
        start_x = -5.2

        for i, (symbol, freq) in enumerate(values):
            node = self.make_node(f"{symbol}: {freq}", [start_x + i*2.6, 1.5, 0])
            nodes.append(node)

        self.play(LaggedStart(*[FadeIn(n) for n in nodes], lag_ratio=0.15))
        self.wait(1)

        # First merge: A(5) + B(9) -> 14
        highlight = SurroundingRectangle(
            VGroup(nodes[0], nodes[1]), buff=0.12
        )
        self.play(Create(highlight))
        self.play(
            nodes[0].animate.shift(DOWN*1.5 + RIGHT*0.7),
            nodes[1].animate.shift(DOWN*1.5 + LEFT*0.7),
        )
        merged14 = self.make_node("14", [0, -1.1, 0])
        self.play(FadeIn(merged14))
        self.play(FadeOut(highlight))

        # Second merge: C(12) + D(13) -> 25
        highlight2 = SurroundingRectangle(
            VGroup(nodes[2], nodes[3]), buff=0.12
        )
        self.play(Create(highlight2))
        c = nodes[2].copy()
        d = nodes[3].copy()
        self.play(
            c.animate.move_to([-3.0, -1.1, 0]),
            d.animate.move_to([-1.0, -1.1, 0]),
        )
        merged25 = self.make_node("25", [-2.0, -2.25, 0])
        self.play(FadeIn(merged25))
        self.play(FadeOut(highlight2))

        # Third merge: 14 + E(16) -> 30
        e = nodes[4].copy()
        self.play(e.animate.move_to([3.0, -1.1, 0]))
        n14 = merged14.copy()
        self.play(n14.animate.move_to([1.0, -1.1, 0]))
        merged30 = self.make_node("30", [2.0, -2.25, 0])
        self.play(FadeIn(merged30))

        # Final root
        root = self.make_node("55", [0, -3.65, 0], width=1.7)
        line1 = Line(merged25.get_bottom(), root.get_top(), buff=0.08)
        line2 = Line(merged30.get_bottom(), root.get_top(), buff=0.08)
        self.play(Create(line1), Create(line2), FadeIn(root))
        self.wait(2)

        codes_title = Text("One valid set of codes", font_size=28)
        codes_title.to_edge(DOWN)

        codes = VGroup(
            Text("C = 00", font_size=22),
            Text("D = 01", font_size=22),
            Text("A = 100", font_size=22),
            Text("B = 101", font_size=22),
            Text("E = 11", font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        codes.next_to(codes_title, UP, buff=0.18)

        self.play(FadeIn(codes_title), FadeIn(codes))
        self.wait(3)
