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



class Year(Scene):
    def construct(self):

        text=MathTex(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )

        self.play(Write(text))
        
        framebox1 = SurroundingRectangle(text[1], buff = .1)
        framebox2 = SurroundingRectangle(text[3], buff = .1)
        self.play(
            ShowCreation(framebox1),
        )
        self.wait()
        self.play(
            ReplacementTransform(framebox1,framebox2),
        )
        self.wait()

        title = Tex(r"This is some \LaTeX")
        basel = MathTex(r"\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}")
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeInFrom(basel, UP),
        )
        self.wait()

        transform_title = Tex("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*[FadeOutAndShift(obj, direction=DOWN) for obj in basel]),
        )
        self.wait()

        grid = NumberPlane()
        grid_title = Tex("This is a grid")
        grid_title.scale(1.5)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeInFrom(grid_title, direction=DOWN),
            ShowCreation(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        grid_transform_title = Tex(
            r"That was a non-linear function \\ applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.animate.apply_function(
                lambda p: p
                          + np.array(
                    [
                        np.sin(p[1]),
                        np.sin(p[0]),
                        0,
                    ]
                )
            ),
            run_time=3,
        )
        self.wait()
        self.play(Transform(grid_title, grid_transform_title))
        self.wait()
