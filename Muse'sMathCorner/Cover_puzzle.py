from manimlib.imports import *

class BeginAnimation(Scene):

    def construct(self):
        BigSquare = Square(side_length = 4.2)
        BigSquare.shift(LEFT * 3)
        start_vector_1 = BigSquare.get_corner(UL)
        end_vector_1 = BigSquare.get_corner(DL)
        end_vector_2 = BigSquare.get_corner(UR)
        line_set_1 = [
            Line(start_vector_1 + RIGHT * 0.6 * i, end_vector_1 + RIGHT * 0.6 * i)
            for i in range(1, 7)
        ]
        line_set_2 = [
            Line(start_vector_1 + DOWN * 0.6 * i, end_vector_2 + DOWN * 0.6 * i)
            for i in range (1, 7)
        ]
        label_x = TextMobject("$2m-1$").scale(0.8).next_to(BigSquare, DOWN)
        label_y = TextMobject("$2n-1$").scale(0.8).next_to(BigSquare, RIGHT).shift(LEFT*0.4)
        label_y.rotate(TAU/4)
        self.play(FadeIn(BigSquare), run_time = 1.5)
        self.play(Write(label_x), run_time = 0.5)
        self.play(Write(label_y), run_time = 0.5)
        for i in range(0, 6):
            self.play(ShowCreation(line_set_1[i]), run_time = 0.1)
        for i in range(0, 6):
            self.play(ShowCreation(line_set_2[i]), run_time = 0.1)
        poly1 = Polygon([3, 2, 0], [3.6, 2, 0], [3.6, 2.6, 0], [4.2, 2.6, 0], [4.2, 3.2, 0], [3, 3.2, 0]).set_fill(BLUE, opacity=0.5)
        poly1.shift(LEFT)
        poly2 = Polygon([4.4, 3.2, 0], [5.6, 3.2, 0], [5.6, 2.6, 0], [6.2, 2.6, 0], [6.2, 2, 0], [5, 2, 0], [5, 2.6, 0], [4.4, 2.6, 0],color = RED).set_fill(RED, opacity=0.5)
        self.play(ShowCreation(poly1), run_time = 1)
        self.play(ShowCreation(poly2), run_time = 2)
        question01 = TextMobject("对于$(2m-1)×(2n-1)$的矩形区域，$m,n\\ge 4，$",color = GREEN).scale(0.6).next_to(label_y, RIGHT).shift(RIGHT*0.4)
        question02 = TextMobject("现有以上这两种瓷砖，可以旋转瓷砖，", color = GREEN).scale(0.6).next_to(question01, DOWN)
        question03 = TextMobject("但是瓷砖边缘要与长方形区域相平行，", color = GREEN).scale(0.6).next_to(question02, DOWN)
        question04 = TextMobject("而且不可以互相重叠，", color = GREEN).scale(0.6).next_to(question03, DOWN)
        question05 = TextMobject("你可以找到将其铺满的最小瓷砖数吗？", color = GREEN).scale(0.6).next_to(question04, DOWN)
        word = TextMobject("No Way!", color = RED).scale(0.6).next_to(poly1, LEFT).shift(LEFT*0.5)
        self.play(Write(question01), Indicate(BigSquare), run_time = 1)
        self.wait(1)
        self.play(Write(question02), run_time = 1)
        self.play(Rotating(poly1, radians = 2*PI, run_time = 1.5))
        self.play(Rotating(poly2, radians = 2*PI, run_time = 1.5))
        self.wait(1)
        self.play(Write(question03), run_time = 1)
        self.play(Write(question04), poly2.shift, LEFT*2.4, run_time = 1)
        self.play(ApplyWave(poly1), ApplyWave(poly2), FadeIn(word), run_time = 1)
        self.play(poly2.shift, RIGHT*2.4, FadeOut(word), run_time = 1)
        self.play(Write(question05), run_time = 1)
        self.wait(3)
        group = VGroup(BigSquare, label_y, label_x, question01, question02, question03, question04, question05, poly1, poly2,
                       line_set_1[0], line_set_1[1], line_set_1[2], line_set_1[3], line_set_1[4], line_set_1[5],
                       line_set_2[0], line_set_2[1], line_set_2[2], line_set_2[3], line_set_2[4], line_set_2[5])
        self.play(FadeOut(group))
        self.wait()


class Part01(Scene):

    def construct(self):
        sentence01 = TextMobject("如果你看过Math's Corner的那篇文章，你肯定对这个问题已经有所了解，甚至有了自己的答案", color = BLUE).scale(0.6).to_edge(UP)
        sentence02 = TextMobject("实际上，我很喜欢这种问题，不需要有什么特定的背景知识，每个人都可以试一试，但往往这样问题的背后蕴含着某个方向的数学知识", color = RED).scale(0.6).next_to(sentence01, DOWN)
        sentence03 = TextMobject("你不妨暂停一下视频，试着自己去画一画", color = RED).scale(0.6).next_to(sentence02, DOWN)
        self.play(Write(sentence01), run_time = 2)
        self.wait(1)
        self.play(Write(sentence02), run_time = 2)
        self.wait(1)
        self.play(Write(sentence03), run_time = 1)
        BigSquare = Square(side_length = 4.2)
        BigSquare.shift(DOWN)
        poly1 = Polygon([3, 2, 0], [3.6, 2, 0], [3.6, 2.6, 0], [4.2, 2.6, 0], [4.2, 3.2, 0], [3, 3.2, 0]).set_fill(BLUE, opacity=0.5)
        poly2 = Polygon([4.4, 3.2, 0], [5.6, 3.2, 0], [5.6, 2.6, 0], [6.2, 2.6, 0], [6.2, 2, 0], [5, 2, 0], [5, 2.6, 0],
                        [4.4, 2.6, 0], color=RED).set_fill(RED, opacity=0.5)
        poly1.shift(DOWN*2)
        poly2.shift(DOWN*2)
        self.play(FadeIn(BigSquare), run_time = 1)
        self.play(FadeIn(poly1), FadeIn(poly2), run_time = 1)
        self.wait(2)
        group = VGroup(sentence01, sentence02, sentence03, BigSquare, poly1, poly2)
        sentence04 = TextMobject("How to cover the rectangle?", color = BLUE).scale(2)
        self.play(ReplacementTransform(group, sentence04), run_time = 1)
        self.wait(2)
        self.play(FadeOut(sentence04))
        self.wait(1)

class Part02(Scene):

    def construct(self):
        sentence01 = TextMobject("我们该如何去思考这个问题？不妨从最简单的形式入手:$m=4,n=4$，所以你能用这两个瓷砖去填满$7×7$的矩形区域吗", color = BLUE).scale(0.6)
        sentence01.to_edge(UP)
        self.play(Write(sentence01), run_time = 1)
        self.wait(1)
        BigSquare = Square(side_length=4.2)
        BigSquare.shift(LEFT * 3)
        start_vector_1 = BigSquare.get_corner(UL)
        end_vector_1 = BigSquare.get_corner(DL)
        end_vector_2 = BigSquare.get_corner(UR)
        line_set_1 = [
            Line(start_vector_1 + RIGHT * 0.6 * i, end_vector_1 + RIGHT * 0.6 * i)
            for i in range(1, 7)
        ]
        line_set_2 = [
            Line(start_vector_1 + DOWN * 0.6 * i, end_vector_2 + DOWN * 0.6 * i)
            for i in range(1, 7)
        ]
        self.play(ShowCreation(BigSquare), run_time = 1)
        for i in range(0, 6):
            self.play(ShowCreation(line_set_1[i]), run_time = 0.1)
        for i in range(0, 6):
            self.play(ShowCreation(line_set_2[i]), run_time = 0.1)
        poly1 = Polygon([3, 2, 0], [3.6, 2, 0], [3.6, 2.6, 0], [4.2, 2.6, 0], [4.2, 3.2, 0], [3, 3.2, 0]).set_fill(BLUE, opacity=0.5).shift(LEFT)
        poly2 = Polygon([4.4, 3.2, 0], [5.6, 3.2, 0], [5.6, 2.6, 0], [6.2, 2.6, 0], [6.2, 2, 0], [5, 2, 0], [5, 2.6, 0],
                        [4.4, 2.6, 0], color=RED).set_fill(RED, opacity=0.5)
        poly1.shift(DOWN*2)
        poly2.shift(DOWN*2)
        self.play(ShowCreation(poly1), ShowCreation(poly2), run_time = 1)
        self.wait(3)
        sv1 = start_vector_1
        ev1 = end_vector_1
        ev2 = end_vector_2
        tile1 = Polygon(sv1, sv1+RIGHT*1.2, sv1+RIGHT*1.2+DOWN*0.6, sv1+RIGHT*1.8+DOWN*0.6, sv1+RIGHT*1.8+DOWN*1.2, sv1+RIGHT*0.6+DOWN*1.2, sv1+RIGHT*0.6+DOWN*0.6, sv1+DOWN*0.6, color = RED).set_fill(RED, opacity=0.5)
        tile2 = Polygon(sv1+RIGHT*1.2, sv1+RIGHT*2.4, sv1+RIGHT*2.4+DOWN*1.2, sv1+RIGHT*1.8+DOWN*1.2,sv1+RIGHT*1.8+DOWN*0.6, sv1+RIGHT*1.2+DOWN*0.6, color = BLUE).set_fill(BLUE, opacity=0.5)
        tile9 = Polygon(sv1+RIGHT*1.2, sv1+RIGHT*2.4, sv1+RIGHT*2.4+DOWN*1.2, sv1+RIGHT*1.8+DOWN*1.2,sv1+RIGHT*1.8+DOWN*0.6, sv1+RIGHT*1.2+DOWN*0.6, color = BLUE).set_fill(BLUE, opacity=0.5).shift(RIGHT*1.8+DOWN*1.2)
        tile10 = Polygon(sv1+RIGHT*1.2, sv1+RIGHT*2.4, sv1+RIGHT*2.4+DOWN*1.2, sv1+RIGHT*1.8+DOWN*1.2,sv1+RIGHT*1.8+DOWN*0.6, sv1+RIGHT*1.2+DOWN*0.6, color = BLUE).set_fill(BLUE, opacity=0.5).shift(DOWN*2.4)
        tile12 = Polygon(sv1+RIGHT*1.2, sv1+RIGHT*2.4, sv1+RIGHT*2.4+DOWN*1.2, sv1+RIGHT*1.8+DOWN*1.2,sv1+RIGHT*1.8+DOWN*0.6, sv1+RIGHT*1.2+DOWN*0.6, color = BLUE).set_fill(BLUE, opacity=0.5).shift(DOWN*2.4+RIGHT*1.8)
        tile3 = Polygon(sv1+RIGHT*1.2, sv1+RIGHT*2.4, sv1+RIGHT*2.4+DOWN*1.2, sv1+RIGHT*1.8+DOWN*1.2,sv1+RIGHT*1.8+DOWN*0.6, sv1+RIGHT*1.2+DOWN*0.6, color = GREEN).shift(RIGHT*1.2).rotate(TAU/4).set_fill(GREEN, opacity=0.5)
        tile11 = Polygon(sv1+RIGHT*1.2, sv1+RIGHT*2.4, sv1+RIGHT*2.4+DOWN*1.2, sv1+RIGHT*1.8+DOWN*1.2,sv1+RIGHT*1.8+DOWN*0.6, sv1+RIGHT*1.2+DOWN*0.6, color = GREEN).shift(RIGHT*1.2).rotate(TAU/4).set_fill(GREEN, opacity=0.5).shift(DOWN*1.8)
        tile8 = Polygon(sv1+RIGHT*1.2, sv1+RIGHT*2.4, sv1+RIGHT*2.4+DOWN*1.2, sv1+RIGHT*1.8+DOWN*1.2,sv1+RIGHT*1.8+DOWN*0.6, sv1+RIGHT*1.2+DOWN*0.6, color = GREEN).shift(RIGHT*1.2).rotate(TAU/4).set_fill(GREEN, opacity=0.5).shift(DOWN*1.2+LEFT*0.6)
        tile13 = Polygon(sv1+RIGHT*1.2, sv1+RIGHT*2.4, sv1+RIGHT*2.4+DOWN*1.2, sv1+RIGHT*1.8+DOWN*1.2,sv1+RIGHT*1.8+DOWN*0.6, sv1+RIGHT*1.2+DOWN*0.6, color = GREEN).shift(RIGHT*1.2).rotate(TAU/4).set_fill(GREEN, opacity=0.5).shift(DOWN*3+LEFT*2.4)
        tile4 = Polygon(sv1+RIGHT*1.2, sv1+RIGHT*2.4, sv1+RIGHT*2.4+DOWN*1.2, sv1+RIGHT*1.8+DOWN*1.2,sv1+RIGHT*1.8+DOWN*0.6, sv1+RIGHT*1.2+DOWN*0.6, color = BLUE).rotate(TAU*3/4).shift(RIGHT*1.8).set_fill(BLUE, opacity=0.5)
        tile7 = Polygon(sv1+RIGHT*1.2, sv1+RIGHT*2.4, sv1+RIGHT*2.4+DOWN*1.2, sv1+RIGHT*1.8+DOWN*1.2,sv1+RIGHT*1.8+DOWN*0.6, sv1+RIGHT*1.2+DOWN*0.6, color = BLUE).rotate(TAU*3/4).shift(RIGHT*1.8).set_fill(BLUE, opacity=0.5).shift(LEFT*2.4+DOWN*1.2)
        tile14 = Polygon(sv1+RIGHT*1.2, sv1+RIGHT*2.4, sv1+RIGHT*2.4+DOWN*1.2, sv1+RIGHT*1.8+DOWN*1.2,sv1+RIGHT*1.8+DOWN*0.6, sv1+RIGHT*1.2+DOWN*0.6, color = BLUE).rotate(TAU*3/4).shift(RIGHT*1.8).set_fill(BLUE, opacity=0.5).shift(LEFT*2.4+DOWN*3)
        tile15 = Polygon(sv1+RIGHT*1.2, sv1+RIGHT*2.4, sv1+RIGHT*2.4+DOWN*1.2, sv1+RIGHT*1.8+DOWN*1.2,sv1+RIGHT*1.8+DOWN*0.6, sv1+RIGHT*1.2+DOWN*0.6, color = GREEN).rotate(TAU*3/4).shift(RIGHT*1.8).set_fill(GREEN, opacity=0.5).shift(LEFT*1.2+DOWN*3)
        tile5 = Polygon(sv1+DOWN*0.6, sv1+DOWN*0.6+RIGHT*0.6,sv1+DOWN*1.2+RIGHT*0.6,sv1+DOWN*1.2+RIGHT*1.2,sv1+DOWN*1.8+RIGHT*1.2,sv1+DOWN*1.8,color = GREEN).set_fill(GREEN, opacity=0.5)
        tile6 = Polygon(sv1+DOWN*0.6, sv1+DOWN*0.6+RIGHT*0.6,sv1+DOWN*1.2+RIGHT*0.6,sv1+DOWN*1.2+RIGHT*1.2,sv1+DOWN*1.8+RIGHT*1.2,sv1+DOWN*1.8,color = GREEN).set_fill(GREEN, opacity=0.5).shift(DOWN*1.2)
        tile16 = Polygon(sv1+DOWN*0.6, sv1+DOWN*0.6+RIGHT*0.6,sv1+DOWN*1.2+RIGHT*0.6,sv1+DOWN*1.2+RIGHT*1.2,sv1+DOWN*1.8+RIGHT*1.2,sv1+DOWN*1.8,color = GREEN).set_fill(GREEN, opacity=0.5).shift(DOWN*2.4+RIGHT*3)
        self.play(TransformFromCopy(poly2, tile1))
        self.play(TransformFromCopy(poly1, tile2))
        self.play(TransformFromCopy(poly1, tile3))
        self.play(TransformFromCopy(poly1, tile4))
        self.play(TransformFromCopy(poly1, tile5))
        self.play(TransformFromCopy(poly1, tile6))
        self.play(TransformFromCopy(poly1, tile7))
        self.play(TransformFromCopy(poly1, tile8))
        self.play(TransformFromCopy(poly1, tile9))
        self.play(TransformFromCopy(poly1, tile10))
        self.play(TransformFromCopy(poly1, tile11))
        self.play(TransformFromCopy(poly1, tile12))
        self.play(TransformFromCopy(poly1, tile13))
        self.play(TransformFromCopy(poly1, tile14))
        self.play(TransformFromCopy(poly1, tile15))
        self.play(TransformFromCopy(poly1, tile16))
        self.wait(3)
        group = VGroup(sentence01, BigSquare, poly1, poly2,  line_set_1[0], line_set_1[1], line_set_1[2], line_set_1[3], line_set_1[4], line_set_1[5],
                       line_set_2[0], line_set_2[1], line_set_2[2], line_set_2[3], line_set_2[4], line_set_2[5], tile1, tile2, tile3,
                       tile4, tile5, tile6, tile7, tile8, tile9, tile10 ,tile11, tile12, tile13, tile14, tile15, tile16)
        self.play(FadeOut(group), run_time = 1)
        self.wait()

class Part03(Scene):

    def construct(self):
        sentence01 = TextMobject("看起来我们已经找到了一种去填满$7×7$方块的方法", color = RED).scale(0.6).to_edge(UP)
        sentence02 = TextMobject("emmmm不过然后呢？", color = RED).scale(0.6).next_to(sentence01, DOWN)
        sentence03 = TextMobject("如果你对俄罗斯方块比较熟悉，也许你会对这种组合非常熟练，想一想你可以利用它们组合成什么样的形状？", color = RED).scale(0.6).to_edge(UP)
        group1 = VGroup(sentence01, sentence02)
        self.play(Write(sentence01), run_time = 1)
        self.wait(1)
        self.play(Write(sentence02), run_time = 1)
        self.wait(2)
        self.play(ReplacementTransform(group1, sentence03), run_time = 1)
        self.wait(1)
        poly1 = Polygon([3, 2, 0], [3.6, 2, 0], [3.6, 2.6, 0], [4.2, 2.6, 0], [4.2, 3.2, 0], [3, 3.2, 0]).rotate(PI/2).set_fill(BLUE, opacity=0.5).to_edge(LEFT).shift(DOWN*1.5)
        poly2 = Polygon([4.4, 3.2, 0], [5.6, 3.2, 0], [5.6, 2.6, 0], [6.2, 2.6, 0], [6.2, 2, 0], [5, 2, 0], [5, 2.6, 0],
                        [4.4, 2.6, 0], color=RED).set_fill(RED, opacity=0.5).next_to(poly1, RIGHT).shift(LEFT*0.8)
        poly3 = Polygon([3, 2, 0], [3.6, 2, 0], [3.6, 2.6, 0], [4.2, 2.6, 0], [4.2, 3.2, 0], [3, 3.2, 0]).rotate(
            3*PI/2).set_fill(BLUE, opacity=0.5).next_to(poly2, RIGHT).shift(LEFT*0.8)
        poly4 = Polygon([3, 2, 0], [3.6, 2, 0], [3.6, 2.6, 0], [4.2, 2.6, 0], [4.2, 3.2, 0], [3, 3.2, 0]).rotate(
            PI / 2).set_fill(BLUE, opacity=0.5).to_edge(LEFT).shift(DOWN*3.5)
        poly5 = Polygon([4.4, 3.2, 0], [5.6, 3.2, 0], [5.6, 2.6, 0], [6.2, 2.6, 0], [6.2, 2, 0], [5, 2, 0], [5, 2.6, 0],
                        [4.4, 2.6, 0], color=RED).set_fill(RED, opacity=0.5).next_to(poly4, RIGHT).shift(LEFT*0.8)
        poly6 = Polygon([4.4, 3.2, 0], [5.6, 3.2, 0], [5.6, 2.6, 0], [6.2, 2.6, 0], [6.2, 2, 0], [5, 2, 0], [5, 2.6, 0],
                        [4.4, 2.6, 0], color=RED).set_fill(RED, opacity=0.5).next_to(poly5, RIGHT).shift(LEFT*0.8)
        poly7 = Polygon([3, 2, 0], [3.6, 2, 0], [3.6, 2.6, 0], [4.2, 2.6, 0], [4.2, 3.2, 0], [3, 3.2, 0]).rotate(
            3 * PI / 2).set_fill(BLUE, opacity=0.5).next_to(poly6, RIGHT).shift(LEFT*0.8)
        poly8 = Polygon([3, 2, 0], [3.6, 2, 0], [3.6, 2.6, 0], [4.2, 2.6, 0], [4.2, 3.2, 0], [3, 3.2, 0]).rotate(
            PI / 2).set_fill(BLUE, opacity=0.5).to_edge(LEFT).shift(DOWN*5.5)
        poly9 = Polygon([4.4, 3.2, 0], [5.6, 3.2, 0], [5.6, 2.6, 0], [6.2, 2.6, 0], [6.2, 2, 0], [5, 2, 0], [5, 2.6, 0],
                        [4.4, 2.6, 0], color=RED).set_fill(RED, opacity=0.5).next_to(poly8, RIGHT).shift(LEFT*0.8)
        poly10 = Polygon([4.4, 3.2, 0], [5.6, 3.2, 0], [5.6, 2.6, 0], [6.2, 2.6, 0], [6.2, 2, 0], [5, 2, 0], [5, 2.6, 0],
                        [4.4, 2.6, 0], color=RED).set_fill(RED, opacity=0.5).next_to(poly9, RIGHT).shift(LEFT*0.8)
        poly11 = Polygon([4.4, 3.2, 0], [5.6, 3.2, 0], [5.6, 2.6, 0], [6.2, 2.6, 0], [6.2, 2, 0], [5, 2, 0], [5, 2.6, 0],
                        [4.4, 2.6, 0], color=RED).set_fill(RED, opacity=0.5).next_to(poly10, RIGHT).shift(LEFT*0.8)
        poly12 = Polygon([3, 2, 0], [3.6, 2, 0], [3.6, 2.6, 0], [4.2, 2.6, 0], [4.2, 3.2, 0], [3, 3.2, 0]).rotate(
            3 * PI / 2).set_fill(BLUE, opacity=0.5).next_to(poly11, RIGHT).shift(LEFT*0.8)
        self.play(FadeIn(poly1))
        self.play(FadeIn(poly2))
        self.play(FadeIn(poly3))
        self.wait(2)
        self.play(FadeIn(poly4))
        self.play(FadeIn(poly5))
        self.play(FadeIn(poly6))
        self.play(FadeIn(poly7))
        self.wait(2)
        self.play(FadeIn(poly8))
        self.play(FadeIn(poly9))
        self.play(FadeIn(poly10))
        self.play(FadeIn(poly11))
        self.play(FadeIn(poly12))
        self.wait(2)
        sentence04 = TextMobject("所以你发现什么规律了吗？", color = RED).scale(0.6).to_edge(UP)
        word = TextMobject("BINGO!", color = YELLOW).next_to(sentence04, DOWN)
        sentence05 = TextMobject("我们可以用k块瓷砖得到任意$2×(2k-1)$的矩形区域！", color = RED).scale(0.6).next_to(sentence04, DOWN)
        self.play(ReplacementTransform(sentence03, sentence04))
        self.wait(1)
        self.play(Write(word), run_time = 1)
        self.wait(1)
        self.play(ReplacementTransform(word, sentence05))
        self.wait(2)
        group2 = VGroup(sentence04, sentence05, poly1, poly2, poly3, poly4, poly5, poly6,
                        poly7, poly8 ,poly9, poly10, poly11, poly12)
        self.play(FadeOut(group2))

class Part04(Scene):

    def construct(self):
        sentence01 = TextMobject("基于以上的结果，你是否可以自己得出答案呢？", color = BLUE).scale(0.6).to_edge(UP)
        sentence02 = TextMobject("再给你一点小提示：矩形的边长均为奇数长度", color = BLUE).scale(0.6).next_to(sentence01, DOWN)
        self.play(Write(sentence01), run_time = 1)
        self.wait(1)
        self.play(Write(sentence02), run_time = 1)
        self.wait(2)
        group1 = VGroup(sentence01, sentence02)
        sentence03 = TextMobject("我们找到了$7×7$区域的覆盖方式，现在我们又可以任意组合成$2×(2k-1)$的矩形", color = RED).scale(0.6).to_edge(UP)
        self.play(ReplacementTransform(group1, sentence03), run_time = 1)
        poly1 = Polygon([-2, 1.5, 0], [2.2, 1.5, 0], [2.2, -2.7, 0],[-2, -2.7, 0], color = BLUE)
        poly2 = Polygon([2.2, 1.5, 0], [3.4, 1.5, 0], [3.4, -2.7, 0],[2.2, -2.7, 0], color = GREEN)
        poly3 = Polygon([-2, -2.7 ,0], [3.4, -2.7, 0],[3.4, -3.9, 0], [-2, -3.9, 0], color = RED)
        self.play(FadeIn(poly1))
        self.wait(0.5)
        self.play(FadeIn(poly2))
        self.wait(0.5)
        self.play(FadeIn(poly3))
        self.wait(2)
        sentence04 = TextMobject("这意味着我们已经找到了覆盖任意奇数边长的矩形的方式！", color = BLUE).scale(0.6).next_to(sentence03, DOWN)
        self.play(Write(sentence04), run_time = 1)
        self.wait(2)
        group2 = VGroup(sentence03, sentence04, poly1, poly2, poly3)
        self.play(FadeOut(group2), run_time = 1)

class Part05(Scene):

    def construct(self):
        sentence01 = TextMobject("$m=4,n=4$时，我们使用了16块瓷砖",color = BLUE).scale(0.6).to_edge(UP)
        sentence02 = TextMobject("每当$m$或$n$增加1时，区域就增加了两行或两列，相应地就增加了n块或m块瓷砖", color = BLUE).scale(0.6).next_to(sentence01, DOWN)
        sentence03 = TextMobject("当然它们也可以同时增加，不难得出以上述方法覆盖，我们的瓷砖数是$mn$！",color = RED).scale(0.6).next_to(sentence02, DOWN)
        tip = TextMobject("如果你对这个结果不是很理解，你可以停下来自己再推导一下，这并不难而且很有趣", color = GREEN).scale(0.5).next_to(sentence03, DOWN)
        self.play(Write(sentence01), run_time = 1)
        self.wait(1)
        self.play(Write(sentence02), run_time = 1)
        self.wait(1)
        self.play(Write(sentence03), run_time = 1)
        self.wait(1)
        self.play(Write(tip), run_time = 1)
        self.wait(2)
        self.play(FadeOut(tip))
        sentence04 = TextMobject("我们得到了一个很整洁的结果$mn$", color = RED).scale(0.6).next_to(sentence03, DOWN)
        self.play(Write(sentence04), run_time = 1)
        self.wait(1)
        word = TextMobject("BUT!问题并没有结束！", color = YELLOW).next_to(sentence03, DOWN)
        self.play(ReplacementTransform(sentence04, word), run_time = 1)
        self.wait(2)
        sentence05 = TextMobject("我们的问题是最小瓷砖数，我们如何去证明这个结果是最小的呢？", color = RED).scale(0.6).next_to(sentence04, DOWN)
        self.play(Write(sentence05), run_time=1)
        self.wait(2)
        group = VGroup(sentence01, sentence02, sentence03, sentence04, sentence05, word)
        self.play(FadeOut(group), run_time = 1)
        self.wait(1)

class Part06(Scene):

    def construct(self):
        sentence01 = TextMobject("如果你想再思考一会儿，可以把视频先停在这儿", color = BLUE).scale(0.6).to_edge(UP)
        self.play(Write(sentence01), run_time = 1)
        self.wait(2)
        self.play(FadeOut(sentence01))
        BigSquare = Square(side_length = 4.2)
        start_vector_1 = BigSquare.get_corner(UL)
        end_vector_1 = BigSquare.get_corner(DL)
        end_vector_2 = BigSquare.get_corner(UR)
        line_set_1 = [
            Line(start_vector_1 + RIGHT * 0.6 * i, end_vector_1 + RIGHT * 0.6 * i)
            for i in range(1, 7)
        ]
        line_set_2 = [
            Line(start_vector_1 + DOWN * 0.6 * i, end_vector_2 + DOWN * 0.6 * i)
            for i in range (1, 7)
        ]
        self.play(Write(BigSquare), run_time = 1)
        for i in range(0, 6):
            self.play(ShowCreation(line_set_1[i]), run_time = 0.1)
        for i in range(0, 6):
            self.play(ShowCreation(line_set_2[i]), run_time = 0.1)
        poly_a = Polygon([3, 2, 0], [3.6, 2, 0], [3.6, 2.6, 0], [4.2, 2.6, 0], [4.2, 3.2, 0], [3, 3.2, 0]).set_fill(BLUE, opacity=0.5)
        poly_b = Polygon([4.4, 3.2, 0], [5.6, 3.2, 0], [5.6, 2.6, 0], [6.2, 2.6, 0], [6.2, 2, 0], [5, 2, 0], [5, 2.6, 0],
                        [4.4, 2.6, 0], color=RED).set_fill(RED, opacity=0.5)
        poly_a.shift(DOWN*2)
        poly_b.shift(DOWN*2)
        self.play(FadeIn(poly_a), FadeIn(poly_b))
        poly1 = Polygon(start_vector_1, start_vector_1+0.6*RIGHT, start_vector_1+0.6*RIGHT+0.6*DOWN, start_vector_1+0.6*DOWN, color = YELLOW).set_fill(YELLOW, opacity=0.5)
        poly2 = Polygon(start_vector_1, start_vector_1+0.6*RIGHT, start_vector_1+0.6*RIGHT+0.6*DOWN, start_vector_1+0.6*DOWN, color = YELLOW).set_fill(YELLOW, opacity=0.5).shift(RIGHT*1.2)
        poly3 = Polygon(start_vector_1, start_vector_1+0.6*RIGHT, start_vector_1+0.6*RIGHT+0.6*DOWN, start_vector_1+0.6*DOWN, color = YELLOW).set_fill(YELLOW, opacity=0.5).shift(RIGHT*2.4)
        poly4 = Polygon(start_vector_1, start_vector_1+0.6*RIGHT, start_vector_1+0.6*RIGHT+0.6*DOWN, start_vector_1+0.6*DOWN, color = YELLOW).set_fill(YELLOW, opacity=0.5).shift(RIGHT*3.6)
        poly5 = Polygon(start_vector_1, start_vector_1+0.6*RIGHT, start_vector_1+0.6*RIGHT+0.6*DOWN, start_vector_1+0.6*DOWN, color = YELLOW).set_fill(YELLOW, opacity=0.5).shift(DOWN*1.2)
        poly6 = Polygon(start_vector_1, start_vector_1+0.6*RIGHT, start_vector_1+0.6*RIGHT+0.6*DOWN, start_vector_1+0.6*DOWN, color = YELLOW).set_fill(YELLOW, opacity=0.5).shift(DOWN*1.2+RIGHT*1.2)
        poly7 = Polygon(start_vector_1, start_vector_1+0.6*RIGHT, start_vector_1+0.6*RIGHT+0.6*DOWN, start_vector_1+0.6*DOWN, color = YELLOW).set_fill(YELLOW, opacity=0.5).shift(DOWN*1.2+RIGHT*2.4)
        poly8 = Polygon(start_vector_1, start_vector_1+0.6*RIGHT, start_vector_1+0.6*RIGHT+0.6*DOWN, start_vector_1+0.6*DOWN, color = YELLOW).set_fill(YELLOW, opacity=0.5).shift(DOWN*1.2+RIGHT*3.6)
        poly9 = Polygon(start_vector_1, start_vector_1+0.6*RIGHT, start_vector_1+0.6*RIGHT+0.6*DOWN, start_vector_1+0.6*DOWN, color = YELLOW).set_fill(YELLOW, opacity=0.5).shift(DOWN*2.4)
        poly10 = Polygon(start_vector_1, start_vector_1+0.6*RIGHT, start_vector_1+0.6*RIGHT+0.6*DOWN, start_vector_1+0.6*DOWN, color = YELLOW).set_fill(YELLOW, opacity=0.5).shift(DOWN*2.4+RIGHT*1.2)
        poly11 = Polygon(start_vector_1, start_vector_1+0.6*RIGHT, start_vector_1+0.6*RIGHT+0.6*DOWN, start_vector_1+0.6*DOWN, color = YELLOW).set_fill(YELLOW, opacity=0.5).shift(DOWN*2.4+RIGHT*2.4)
        poly12 = Polygon(start_vector_1, start_vector_1+0.6*RIGHT, start_vector_1+0.6*RIGHT+0.6*DOWN, start_vector_1+0.6*DOWN, color = YELLOW).set_fill(YELLOW, opacity=0.5).shift(DOWN*2.4+RIGHT*3.6)
        poly13 = Polygon(start_vector_1, start_vector_1+0.6*RIGHT, start_vector_1+0.6*RIGHT+0.6*DOWN, start_vector_1+0.6*DOWN, color = YELLOW).set_fill(YELLOW, opacity=0.5).shift(DOWN*3.6)
        poly14 = Polygon(start_vector_1, start_vector_1+0.6*RIGHT, start_vector_1+0.6*RIGHT+0.6*DOWN, start_vector_1+0.6*DOWN, color = YELLOW).set_fill(YELLOW, opacity=0.5).shift(DOWN*3.6+RIGHT*1.2)
        poly15 = Polygon(start_vector_1, start_vector_1+0.6*RIGHT, start_vector_1+0.6*RIGHT+0.6*DOWN, start_vector_1+0.6*DOWN, color = YELLOW).set_fill(YELLOW, opacity=0.5).shift(DOWN*3.6+RIGHT*2.4)
        poly16 = Polygon(start_vector_1, start_vector_1+0.6*RIGHT, start_vector_1+0.6*RIGHT+0.6*DOWN, start_vector_1+0.6*DOWN, color = YELLOW).set_fill(YELLOW, opacity=0.5).shift(DOWN*3.6+RIGHT*3.6)
        self.wait(1)
        self.play(FadeIn(poly1))
        self.play(FadeIn(poly2))
        self.play(FadeIn(poly3))
        self.play(FadeIn(poly4))
        self.play(FadeIn(poly5))
        self.play(FadeIn(poly6))
        self.play(FadeIn(poly7))
        self.play(FadeIn(poly8))
        self.play(FadeIn(poly9))
        self.play(FadeIn(poly10))
        self.play(FadeIn(poly11))
        self.play(FadeIn(poly12))
        self.play(FadeIn(poly13))
        self.play(FadeIn(poly14))
        self.play(FadeIn(poly15))
        self.play(FadeIn(poly16))
        self.wait(2)
        sentence02 = TextMobject("观察这些被填充了的方格，对于题中所给的两种瓷砖在覆盖该区域时，每个瓷砖至多覆盖这些被填充方格中的一个", color = BLUE).scale(0.6).next_to(sentence01, DOWN)
        self.play(Write(sentence02))
        self.wait(2)
        sentence03 = TextMobject("换句话说，我们至少需要被填充方格数目的瓷砖去覆盖区域", color = BLUE).scale(0.6).next_to(BigSquare, DOWN*0.5)
        self.play(Write(sentence03))
        self.wait(2)
        sentence04 = TextMobject("而对于$(2m-1)×(2n-1)$的区域", color = GREEN).scale(0.6).to_edge(LEFT).shift(UP)
        sentence05 = TextMobject("被填充方格数正是$mn$个！", color = RED).scale(0.8).next_to(sentence04, DOWN)
        self.play(Write(sentence04), run_time = 1)
        self.wait(1)
        self.play(Write(sentence05), run_time = 1)
        self.wait(2)
        group = VGroup( sentence02, sentence03, sentence04, sentence05, poly1, poly2, poly3, poly4, poly5, poly6, poly7, poly8
                       ,poly9, poly10, poly11, poly12, poly13, poly14, poly15, poly16, poly_a, poly_b, BigSquare,line_set_1[0], line_set_1[1],
                       line_set_1[2], line_set_1[3], line_set_1[4], line_set_1[5],line_set_2[0], line_set_2[1], line_set_2[2], line_set_2[3], line_set_2[4], line_set_2[5])
        self.play(FadeOut(group), run_time = 1)

class Part07(Scene):

    def construct(self):
        sentence01 = TextMobject("现在让我们回过头来去看这道有趣的题目，尽管并不是特别复杂，但是依然体现了一些数学思想，比如分治(Divide and Conquer)", color = BLUE).scale(0.6).to_edge(UP)
        sentence02 = TextMobject("需要指出在处理7×7区域的填充问题时，Up除了慢慢试没有其他的方法，但是如果理解了上一部分的被填充方格数，这个问题也就变得简单了！", color = GREEN).scale(0.6).next_to(sentence01, DOWN)
        sentence03 = TextMobject("当然我想也会有其他巧妙的方法，如果你有自己的idea,欢迎与Up交流！", color = BLUE).scale(0.6).next_to(sentence01, DOWN)
        sentence04 = TextMobject("Keep Thinking!", color = RED).scale(0.8).next_to(sentence03, DOWN)
        sentence05 = TextMobject("结尾彩蛋：俄罗斯方块中本题目中四格方块的名字", color = GREEN).scale(0.6).next_to(sentence04, DOWN)
        poly1 = Polygon([-2, 0, 0], [0, 0 ,0], [0, -1, 0], [1, -1, 0],[1, -2, 0], [-1, -2, 0],[-1, -1 ,0],[-2, -1, 0], color = RED).set_fill(RED, opacity=0.5)
        word = TextMobject("Cleveland Z", color = RED).scale(0.8).next_to(poly1, DOWN)
        group = VGroup(sentence01, sentence05, sentence03, sentence04, poly1, word)
        self.play(Write(sentence01),run_time = 1.5)
        self.wait(1)
        self.play(FadeIn(sentence02), run_time = 1)
        self.wait(2)
        self.play(FadeOut(sentence02))
        self.wait(1)
        self.play(Write(sentence03), run_time = 1)
        self.wait(1)
        self.play(DrawBorderThenFill(sentence04), run_time = 1)
        self.wait(2)
        self.play(Write(sentence05), run_time = 1)
        self.wait(1)
        self.play(FadeIn(poly1), Write(word), run_time = 1)
        self.wait(3)
        self.play(FadeOut(group))