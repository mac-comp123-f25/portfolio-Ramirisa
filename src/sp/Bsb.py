import turtle as T
import math

# ---------- screen ----------
SCREEN_W, SCREEN_H = 1000, 800
scr = T.Screen()
scr.setup(SCREEN_W, SCREEN_H)
scr.title("Ballpark: Stripes, Infield Dirt, Foul Lines, Fence & Bases")
scr.bgcolor("#5fd36a")
scr.tracer(False)

pen = T.Turtle(visible=False)
pen.speed(0)

# ---------- stripe colors ----------
LIGHT = "#6fdc6f"
DARK  = "#2e8b57"
STRIPE_W = 40

def draw_vertical_grass(width=SCREEN_W, height=SCREEN_H, stripe_w=STRIPE_W,
                        colors=(LIGHT, DARK)):
    left = -width // 2
    bottom = -height // 2
    x = left
    i = 0
    while x < width // 2:
        pen.penup()
        pen.goto(x, bottom)
        pen.setheading(90)
        pen.color(colors[i % 2], colors[i % 2])
        pen.begin_fill()
        pen.pendown()
        pen.forward(height)
        pen.right(90)
        pen.forward(stripe_w)
        pen.right(90)
        pen.forward(height)
        pen.end_fill()
        pen.right(90)
        x += stripe_w
        i += 1

# ---------- geometry helpers ----------
def diamond_corners(home, diag_len):
    hx, hy = home
    side = diag_len / math.sqrt(2)
    home_c = (hx, hy)
    first  = (hx + side/2, hy + side/2)
    second = (hx,          hy + side)
    third  = (hx - side/2, hy + side/2)
    return home_c, first, second, third

# ---------- infield dirt ----------
def draw_infield_dirt(HOME):
    DIRT = "#d2a679"
    OUTER_DIAG = 650
    INNER_DIAG = 400
    MOUND_R = 35

    field = T.Turtle(visible=False)
    field.speed(0)
    field.penup()

    home_c, first, second, third = diamond_corners(HOME, OUTER_DIAG)
    field.color(DIRT, DIRT)
    field.goto(*home_c); field.pendown(); field.begin_fill()
    for pt in (first, second, third, home_c):
        field.goto(*pt)
    field.end_fill(); field.penup()

    inner_home, i1, i2, i3 = diamond_corners(HOME, INNER_DIAG)
    field.color(scr.bgcolor(), scr.bgcolor())
    field.goto(*inner_home); field.pendown(); field.begin_fill()
    for pt in (i1, i2, i3, inner_home):
        field.goto(*pt)
    field.end_fill(); field.penup()

    # mound
    t = 0.475
    mx = home_c[0] + (second[0] - home_c[0]) * t
    my = home_c[1] + (second[1] - home_c[1]) * t
    field.color(DIRT, DIRT)
    field.goto(mx, my - MOUND_R - 70); field.pendown()
    field.begin_fill(); field.circle(MOUND_R); field.end_fill()
    field.penup()

# ---------- BASES ----------
BASES_DIAG = 475
BASE_SIZE = 14
HOME_SIZE = 26

# You can adjust these individually:
HOME_OFFSET  = (-5, 0)
FIRST_OFFSET = (-20, 0)
SECOND_OFFSET = (-10, 0)
THIRD_OFFSET = (0, 0)

def _draw_diamond_base_at_corner(pos, size=BASE_SIZE):
    t = T.Turtle(visible=False); t.speed(0); t.color("white"); t.fillcolor("white"); t.penup()
    x, y = pos
    t.goto(x, y)
    t.setheading(45)
    t.begin_fill(); t.pendown()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill(); t.penup()

def _home_plate_vertices(home, width=HOME_SIZE, offset=(0,0)):
    ox, oy = offset
    home = (home[0] + ox, home[1] + oy)
    f1 = (math.sqrt(0.5),  math.sqrt(0.5))
    f3 = (-math.sqrt(0.5), math.sqrt(0.5))
    u  = (0.0, 1.0)
    w  = (1.0, 0.0)
    s = width
    d = s * 0.60
    P0 = home
    P1 = (home[0] + f3[0]*(s/2), home[1] + f3[1]*(s/2))
    P2 = (P1[0] + u[0]*d, P1[1] + u[1]*d)
    P3 = (P2[0] + w[0]*s, P2[1] + w[1]*s)
    P4 = (P3[0] - u[0]*d, P3[1] - u[1]*d)
    P5 = (home[0] + f1[0]*(s/2), home[1] + f1[1]*(s/2))
    return [P0, P1, P2, P3, P4, P5, P0]

def draw_home_plate(HOME):
    t = T.Turtle(visible=False); t.speed(0); t.color("white"); t.fillcolor("white"); t.penup()
    verts = _home_plate_vertices(HOME, HOME_SIZE, HOME_OFFSET)
    t.goto(*verts[0]); t.begin_fill(); t.pendown()
    for p in verts[1:]:
        t.goto(*p)
    t.end_fill(); t.penup()

def draw_first_base(HOME):
    _, first, _, _ = diamond_corners(HOME, BASES_DIAG)
    x = first[0] + FIRST_OFFSET[0]
    y = first[1] + FIRST_OFFSET[1]
    _draw_diamond_base_at_corner((x, y), BASE_SIZE)

def draw_second_base(HOME):
    _, _, second, _ = diamond_corners(HOME, BASES_DIAG)
    x = second[0] + SECOND_OFFSET[0]
    y = second[1] + SECOND_OFFSET[1]
    _draw_diamond_base_at_corner((x, y), BASE_SIZE)

def draw_third_base(HOME):
    _, _, _, third = diamond_corners(HOME, BASES_DIAG)
    x = third[0] + THIRD_OFFSET[0]
    y = third[1] + THIRD_OFFSET[1]
    _draw_diamond_base_at_corner((x, y), BASE_SIZE)

# ---------- foul lines ----------
def draw_foul_lines(HOME):
    FOUL_LEN = 1300
    lines = T.Turtle(visible=False)
    lines.speed(0)
    lines.pensize(6)
    lines.color("white")
    lines.penup()
    lines.goto(*HOME)
    lines.dot(10, "white")

    for angle in (45, 135):
        lines.penup()
        lines.goto(*HOME)
        lines.setheading(angle)
        lines.pendown()
        lines.forward(FOUL_LEN)
        lines.penup()

# ---------- outfield fence ----------
def draw_outfield_arc(HOME):
    FENCE_RADIUS = 720
    ARC_WIDTH = 8
    fence = T.Turtle(visible=False)
    fence.speed(0)
    fence.color("white")
    fence.width(ARC_WIDTH)
    fence.penup()

    cx, cy = HOME
    first = True
    for deg in range(135, 46, -2):
        r = math.radians(deg)
        x = cx + FENCE_RADIUS * math.cos(r)
        y = cy + FENCE_RADIUS * math.sin(r)
        if first:
            fence.goto(x, y); fence.pendown(); first = False
        else:
            fence.goto(x, y)
    fence.penup()

# ---------- draw everything ----------
HOME = (0, -320)
draw_vertical_grass()
draw_infield_dirt(HOME)

draw_home_plate(HOME)
draw_first_base(HOME)
draw_second_base(HOME)
draw_third_base(HOME)

draw_foul_lines(HOME)
draw_outfield_arc(HOME)

# ===================== BAT: choose color + swing on Space =====================
bat_color = scr.textinput("Bat Color", "Type a color (e.g. saddlebrown or #8B4513):")
if not bat_color:
    bat_color = "saddlebrown"

# Shift the bat handle (pivot) left/right/up/down
PIVOT_OFFSET = (-20, 5)  # negative x = left, positive x = right
PIVOT = (HOME[0] + PIVOT_OFFSET[0], HOME[1] + PIVOT_OFFSET[1])

BAT_LEN = 50
BAT_W = 5
BASE_ANGLE = 40
AIM_OFFSET = -50

bat = T.Turtle(visible=False)
bat.speed(0)
bat.color(bat_color)
bat.fillcolor(bat_color)
bat.penup()

# --- CHANGED: track CURRENT_HEADING + angular speed for realistic hits ---
CURRENT_HEADING = 0.0
PREV_HEADING = 0.0
BAT_OMEGA_DEG = 0.0   # change in heading (deg) since last frame

def draw_bat_at_heading(heading):
    global CURRENT_HEADING, PREV_HEADING, BAT_OMEGA_DEG

    # compute angular speed (deg/frame)
    PREV_HEADING, CURRENT_HEADING = CURRENT_HEADING, heading
    BAT_OMEGA_DEG = CURRENT_HEADING - PREV_HEADING

    bat.clear()
    bat.penup()
    bat.goto(PIVOT)
    bat.setheading(heading)
    bat.left(90); bat.forward(BAT_W/2); bat.right(90)
    bat.begin_fill(); bat.pendown()
    bat.forward(BAT_LEN)
    bat.right(90); bat.forward(BAT_W)
    bat.right(90); bat.forward(BAT_LEN)
    bat.right(90); bat.forward(BAT_W)
    bat.end_fill(); bat.penup()
    bat.goto(PIVOT)
    bat.dot(max(6, int(BAT_W*0.6)), "white")


def redraw_bat():
    draw_bat_at_heading(BASE_ANGLE + AIM_OFFSET)
    scr.update()

swinging = False

def swing():
    global swinging
    if swinging:
        return
    swinging = True
    start = BASE_ANGLE + AIM_OFFSET
    peak = start + 100
    step = 3
    a = start
    while a <= peak:
        draw_bat_at_heading(a); scr.update(); a += step
    while a >= start:
        draw_bat_at_heading(a); scr.update(); a -= step
    swinging = False

def change_color():
    global bat_color
    c = scr.textinput("Bat Color", "New color (name or hex):")
    if c:
        bat_color = c
        bat.color(bat_color)
        bat.fillcolor(bat_color)
        redraw_bat()

# key bindings
scr.onkey(swing, "space")
scr.onkey(change_color, "c")
scr.listen()

redraw_bat()
# =====================================================================

# ===================== BALLS: pitch from mound; bat can hit =====================
BALL_R = 6              # ball radius (px)
BALL_SPEED = 8          # inbound speed toward home
LAUNCH_SPEED = 14       # speed after a hit
THROW_INTERVAL = 1400   # ms between pitches
TICK_MS = 20            # physics timestep (ms)

balls = []              # [{t, vx, vy, hit}]

def _mound_center(HOME):
    """Match mound used when drawing: 47.5% toward second, then -70 px."""
    OUTER_DIAG = 650
    side = OUTER_DIAG / math.sqrt(2)
    home_c = (HOME[0], HOME[1])
    second = (HOME[0], HOME[1] + side)
    t = 0.475
    mx = home_c[0] + (second[0] - home_c[0]) * t
    my = home_c[1] + (second[1] - home_c[1]) * t
    return (mx, my - 70)

def _unit(vx, vy):
    L = math.hypot(vx, vy)
    return (vx / L, vy / L) if L else (0.0, 0.0)

def _spawn_ball():
    """Create a new ball at the mound, headed over the middle of home plate."""
    start = _mound_center(HOME)

    # --- target = middle of home plate's flat edge (uses your existing geometry) ---
    verts = _home_plate_vertices(HOME, HOME_SIZE, HOME_OFFSET)
    P2, P3 = verts[2], verts[3]                 # endpoints of the flat edge facing second
    target = ((P2[0] + P3[0]) / 2, (P2[1] + P3[1]) / 2)

    # ball turtle
    ball = T.Turtle(visible=False)
    ball.speed(0)
    ball.shape("circle")
    s = (2*BALL_R) / 20.0                       # default circle is 20px diameter
    ball.shapesize(s, s)
    ball.color("white")
    ball.penup()
    ball.goto(start)
    ball.showturtle()

    # velocity toward the target (center over the plate)
    dx = target[0] - start[0]
    dy = target[1] - start[1]
    ux, uy = _unit(dx, dy)
    vx, vy = BALL_SPEED * ux, BALL_SPEED * uy

    balls.append({"t": ball, "vx": vx, "vy": vy, "hit": False})

    # schedule next pitch
    scr.ontimer(_spawn_ball, THROW_INTERVAL)


def _bat_contact_details(ball_xy):
    """Return (hit_bool, s_along_bat, d_perp) for collision check.
       s_along_bat: 0 at the handle, BAT_LEN at the tip.
       d_perp: perpendicular distance from bat axis."""
    bx, by = ball_xy
    vx = bx - PIVOT[0]
    vy = by - PIVOT[1]

    th = math.radians(CURRENT_HEADING)
    ux, uy = math.cos(th), math.sin(th)   # unit along bat axis

    # decomposition of vector to ball
    s = vx*ux + vy*uy                     # along-bat coordinate
    px = vx - s*ux
    py = vy - s*uy
    d_perp = math.hypot(px, py)

    on_length = (0 <= s <= BAT_LEN)
    close_enough = d_perp <= (BAT_W/2 + BALL_R)
    return (on_length and close_enough, s, d_perp)


def _tick():
    """Advance balls, check collisions, cull offscreen."""
    for b in list(balls):
        turt = b["t"]
        x = turt.xcor() + b["vx"]
        y = turt.ycor() + b["vy"]
        turt.goto(x, y)

        if not b["hit"]:
            hit, s_along, d_perp = _bat_contact_details((x, y))
            if hit:
                b["hit"] = True

                # --- contact timing -> spray angle (flipped so EARLY -> LEFT) ---
                contact_phase = max(0.0, min(1.0, s_along / BAT_LEN))
                MAX_SPRAY_DEG = -40.0  # you can keep 35.0 if you prefer
                SPRAY_BIAS_DEG = 60.0  # small constant nudge toward LF (tweak 0–6)

                # Flip the sign: early (near handle, small s_along) → positive spray (toward LF)
                spray_deg = (0.5 - contact_phase) * 2.0 * MAX_SPRAY_DEG + SPRAY_BIAS_DEG

                launch_deg = CURRENT_HEADING + spray_deg

                # final launch angle: bat heading plus spray
                launch_deg = CURRENT_HEADING + spray_deg
                th = math.radians(launch_deg)

                # --- exit velo: base + bat speed + centered contact bonus ---
                CENTER_BONUS = 4.0
                BAT_SPEED_GAIN = 0.25
                centered = max(0.0, 1.0 - (d_perp / (BAT_W/2 + BALL_R)))  # 0..1
                exit_speed = LAUNCH_SPEED + BAT_SPEED_GAIN*abs(BAT_OMEGA_DEG) + CENTER_BONUS*centered

                b["vx"] = exit_speed * math.cos(th)
                b["vy"] = exit_speed * math.sin(th)


        if (abs(x) > SCREEN_W/2 + 80) or (abs(y) > SCREEN_H/2 + 80):
            turt.hideturtle()
            balls.remove(b)

    scr.update()
    scr.ontimer(_tick, TICK_MS)

# start pitching + physics loop
_spawn_ball()
_tick()
# =============================================================================

scr.update()
T.done()













