from manim import *


class FollowingGraphCamera(GraphScene, MovingCameraScene):
    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)

    def construct(self):
        self.camera_frame.save_state()
        self.setup_axes(animate=False)
        graph = self.get_graph(lambda x: np.sin(x),
                               color=BLUE,
                               x_min=0,
                               x_max=3 * PI
                               )
        moving_dot = Dot().move_to(graph.points[0]).set_color(ORANGE)

        dot_at_start_graph = Dot().move_to(graph.points[0])
        dot_at_end_graph = Dot().move_to(graph.points[-1])
        self.add(graph, dot_at_end_graph, dot_at_start_graph, moving_dot)
        self.play(self.camera_frame.animate.scale(0.5).move_to(moving_dot))

        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera_frame.add_updater(update_curve)
        self.play(MoveAlongPath(moving_dot, graph, rate_func=linear))
        self.camera_frame.remove_updater(update_curve)

        self.play(Restore(self.camera_frame))


class Node(Scene):
    def construct(self):

        waveeqn = MathTex(
            "v = f \\times \\lambda "
        )
        self.play(
            FadeIn(waveeqn)
        )
        self.wait()

        text = MathTex(
            "f=",
            "v",
            "\\times",
            "\\frac{1}{\lambda }"
        )
        self.play(
            Transform(waveeqn, text)
        )
        self.wait()

        text2 = MathTex(
            "f=",
            "v",
            "\\times",
            "\\frac{1}{ 2L }"
        )
        self.play(
            Transform(waveeqn, text2)
        )
        self.wait()
        framebox1 = SurroundingRectangle(text2[3], buff=.1)
        framebox2 = SurroundingRectangle(text2[1], buff=.1)
        self.play(
            ShowCreation(framebox1),
        )
        self.wait()

        transform_title = Tex(
            "L = Uncovering the holes"
        )

        transform_title.to_corner(DOWN + LEFT)
        self.play(
            FadeIn(transform_title)
        )
        self.wait()

        self.play(
            ReplacementTransform(framebox1, framebox2),
        )

        self.wait()

        transform_title2 = Tex(
            "v = Increasing air speed"
        )

        transform_title2.to_corner(DOWN + LEFT)
        self.play(
            Transform(transform_title, transform_title2)
        )
        self.wait(3)
