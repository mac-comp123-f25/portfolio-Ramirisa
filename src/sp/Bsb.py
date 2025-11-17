import turtle as T
import math

# ---------- screen -------------------------------------------------------------------------------
SCREEN_W, SCREEN_H = 1000, 800
scr = T.Screen()
scr.setup(SCREEN_W, SCREEN_H)
scr.title("Ballpark: Stripes, Infield Dirt, Foul Lines, Fence & Bases")
scr.bgcolor("#5fd36a")
scr.tracer(False)

pen = T.Turtle(visible=False)
pen.speed(0)

# ---------- stripe colors for Outfield grass -----------------------------------------------------
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

# ---------- helper for bases ----------------------------------------------------------
def diamond_corners(home, diag_len):
    hx, hy = home
    side = diag_len / math.sqrt(2)
    home_c = (hx, hy)
    first  = (hx + side/2, hy + side/2)
    second = (hx,          hy + side)
    third  = (hx - side/2, hy + side/2)
    return home_c, first, second, third

# ---------- infield dirt ----------------------------------------------------------------
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

# adjusting base position
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
    ox, oy = offset                         # how much to nudge home plate left/right/up/down
    home = (home[0] + ox, home[1] + oy)     # apply that offset to the home-plate point

    # unit directions for the two foul lines (45° and 135° from horizontal)
    f1 = (math.sqrt(0.5),  math.sqrt(0.5))  # points up-right
    f3 = (-math.sqrt(0.5), math.sqrt(0.5))  # points up-left
    u  = (0.0, 1.0)                         # up direction toward second base (used to add depth)
    w  = (1.0, 0.0)                         # right direction (used to make the flat top edge)
    s = width                               # total width across the flat top of home plate
    d = s * 0.60                            # how deep the rectangular section goes upward
    P0 = home                               # tip of home plate (the pointy bottom)
    P1 = (home[0] + f3[0]*(s/2), home[1] + f3[1]*(s/2))   # go half-width up-left along the 3B foul line
    P2 = (P1[0] + u[0]*d, P1[1] + u[1]*d)                 # from there, go up by depth d
    P3 = (P2[0] + w[0]*s, P2[1] + w[1]*s)                 # move to the right by the full width s
    P4 = (P3[0] - u[0]*d, P3[1] - u[1]*d)                 # come back down by depth d
    P5 = (home[0] + f1[0]*(s/2), home[1] + f1[1]*(s/2))   # half-width up-right along the 1B foul line
    return [P0, P1, P2, P3, P4, P5, P0]     # loop back to P0 to close the shape

def draw_home_plate(HOME):
    t = T.Turtle(visible=False); t.speed(0)
    t.color("white"); t.fillcolor("white"); t.penup()
    verts = _home_plate_vertices(HOME, HOME_SIZE, HOME_OFFSET)  # compute the 6 points of home plate
    t.goto(*verts[0]); t.begin_fill(); t.pendown()
    for p in verts[1:]:                    # draw lines through each vertex in order
        t.goto(*p)
    t.end_fill(); t.penup()

def draw_first_base(HOME):
    _, first, _, _ = diamond_corners(HOME, BASES_DIAG)   # get first base corner from the diamond
    x = first[0] + FIRST_OFFSET[0]                       # nudge with your custom offset
    y = first[1] + FIRST_OFFSET[1]
    _draw_diamond_base_at_corner((x, y), BASE_SIZE)      # draw a small diamond here

def draw_second_base(HOME):
    _, _, second, _ = diamond_corners(HOME, BASES_DIAG)  # get second base corner
    x = second[0] + SECOND_OFFSET[0]
    y = second[1] + SECOND_OFFSET[1]
    _draw_diamond_base_at_corner((x, y), BASE_SIZE)

def draw_third_base(HOME):
    _, _, _, third = diamond_corners(HOME, BASES_DIAG)   # get third base corner
    x = third[0] + THIRD_OFFSET[0]
    y = third[1] + THIRD_OFFSET[1]
    _draw_diamond_base_at_corner((x, y), BASE_SIZE)


# ---------- foul lines --------------------------------------------------------------
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
    FENCE_RADIUS = 720                   # how far the fence is from home plate
    ARC_WIDTH = 8                        # thickness of the fence line
    fence = T.Turtle(visible=False); fence.speed(0)
    fence.color("white"); fence.width(ARC_WIDTH); fence.penup()

    cx, cy = HOME                        # center the arc around home plate
    first = True
    for deg in range(135, 46, -2):       # sweep from left foul (135°) to right foul (45°)
        r = math.radians(deg)            # convert degrees to radians for sin/cos
        x = cx + FENCE_RADIUS * math.cos(r)  # x = center_x + radius * cos(angle)
        y = cy + FENCE_RADIUS * math.sin(r)  # y = center_y + radius * sin(angle)
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
    if swinging:                         # ignore if already swinging to prevent overlap
        return
    swinging = True
    start = BASE_ANGLE + AIM_OFFSET      # where the bat starts
    peak = start + 100                   # how far the bat will travel in the swing
    step = 3                             # how many degrees to move each frame
    a = start
    while a <= peak:                     # forward part of the swing
        draw_bat_at_heading(a)           # draw bat at angle a
        scr.update()                     # push frame to screen
        a += step
    while a >= start:                    # return the bat back to start
        draw_bat_at_heading(a)
        scr.update()
        a -= step
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
BALL_R = 6              # ball radius
BALL_SPEED = 8          # inbound speed toward home
LAUNCH_SPEED = 14       # speed after a hit
THROW_INTERVAL = 1400   # ms between pitches
TICK_MS = 20            # physics timestep

balls = []              # [{t, vx, vy, hit}]

def _mound_center(HOME):
    OUTER_DIAG = 650
    side = OUTER_DIAG / math.sqrt(2)     # side length of the infield’s big diamond
    home_c = (HOME[0], HOME[1])          # home point
    second = (HOME[0], HOME[1] + side)   # second base is straight up by one side
    t = 0.475                            # mound is about 47.5% of the way from home to second
    mx = home_c[0] + (second[0] - home_c[0]) * t   # x along the line home→second
    my = home_c[1] + (second[1] - home_c[1]) * t   # y along the line home→second
    return (mx, my - 70)                 # shift down a little so the drawn mound circle matches


def _unit(vx, vy):
    L = math.hypot(vx, vy)               # length of the vector
    return (vx / L, vy / L) if L else (0.0, 0.0)  # divide by length to make it length 1 (unit vector)


def _spawn_ball():
    start = _mound_center(HOME)                      # where the pitch starts (the mound)

    verts = _home_plate_vertices(HOME, HOME_SIZE, HOME_OFFSET)  # outline of home plate
    P2, P3 = verts[2], verts[3]                     # the two corners of the flat top edge
    target = ((P2[0] + P3[0]) / 2, (P2[1] + P3[1]) / 2)  # aim for the middle of that edge

    ball = T.Turtle(visible=False); ball.speed(0)
    ball.shape("circle"); s = (2*BALL_R) / 20.0     # scale the default 20px circle to our BALL_R
    ball.shapesize(s, s); ball.color("white")
    ball.penup(); ball.goto(start); ball.showturtle()

    dx = target[0] - start[0]                       # vector from mound to plate center (x)
    dy = target[1] - start[1]                       # vector from mound to plate center (y)
    ux, uy = _unit(dx, dy)                          # normalize to get direction only
    vx, vy = BALL_SPEED * ux, BALL_SPEED * uy       # multiply by speed to get velocity

    balls.append({"t": ball, "vx": vx, "vy": vy, "hit": False})  # store this ball’s state
    scr.ontimer(_spawn_ball, THROW_INTERVAL)        # schedule the next pitch



def _bat_contact_details(ball_xy):
    bx, by = ball_xy                                # ball position
    vx = bx - PIVOT[0]; vy = by - PIVOT[1]          # vector from bat pivot (handle) to ball

    th = math.radians(CURRENT_HEADING)              # bat’s current angle in radians
    ux, uy = math.cos(th), math.sin(th)             # unit vector along the bat’s long axis

    s = vx*ux + vy*uy                               # projection length along the bat (dot product)
    px = vx - s*ux; py = vy - s*uy                  # perpendicular (shortest) vector from bat to ball
    d_perp = math.hypot(px, py)                     # distance from bat line to ball center

    on_length = (0 <= s <= BAT_LEN)                 # is the contact point between handle and tip?
    close_enough = d_perp <= (BAT_W/2 + BALL_R)     # is the ball close enough to touch the bat?
    return (on_length and close_enough, s, d_perp)  # return collision + where it hit + miss distance


# ---------- HUD banner ----------
hud = T.Turtle(visible=False)
hud.hideturtle()
hud.penup()

def show_banner(msg, color="white", duration=1200):
    hud.clear()
    hud.color(color)
    hud.goto(0, SCREEN_H/2 - 100)   # top center
    hud.write(msg, align="center", font=("Arial", 36, "bold"))
    # auto-clear after duration ms
    scr.ontimer(lambda: hud.clear(), duration)



def _tick():
    for b in list(balls):                           # loop through all active balls
        turt = b["t"]
        x = turt.xcor() + b["vx"]                   # move ball by its velocity x
        y = turt.ycor() + b["vy"]                   # move ball by its velocity y
        turt.goto(x, y)

        if not b["hit"]:                            # only check collision before it’s hit
            hit, s_along, d_perp = _bat_contact_details((x, y))
            if hit:
                b["hit"] = True                     # mark as hit so we don’t re-hit it

                contact_phase = max(0.0, min(1.0, s_along / BAT_LEN))  # 0 (handle) .. 1 (tip)

                # timing-to-angle mapping:
                # MAX_SPRAY_DEG is the maximum angle change based on timing
                # SPRAY_BIAS_DEG adds a constant nudge toward a side
                MAX_SPRAY_DEG = -40.0               # the farthest the ball can go toward right field
                SPRAY_BIAS_DEG = 60.0               # make sure balls can be hit to left field as well

                # convert timing to spray: early vs. late changes direction
                spray_deg = (0.5 - contact_phase) * 2.0 * MAX_SPRAY_DEG + SPRAY_BIAS_DEG

                launch_deg = CURRENT_HEADING + spray_deg  # bat aim + timing spray
                th = math.radians(launch_deg)

                # exit speed = base speed + speed from swing + bonus for centered contact
                CENTER_BONUS = 4.0
                BAT_SPEED_GAIN = 0.25
                centered = max(0.0, 1.0 - (d_perp / (BAT_W/2 + BALL_R)))  # 1.0 if perfectly centered
                exit_speed = LAUNCH_SPEED + BAT_SPEED_GAIN*abs(BAT_OMEGA_DEG) + CENTER_BONUS*centered

                b["vx"] = exit_speed * math.cos(th)  # new x velocity from launch angle and speed
                b["vy"] = exit_speed * math.sin(th)  # new y velocity from launch angle and speed

                # call fair or foul using launch angle:
                # 0° = right, 90° = up. Fair if between 45° and 135° and going upward.
                ang = math.degrees(math.atan2(b["vy"], b["vx"]))
                if 45.0 <= ang <= 135.0 and b["vy"] > 0:
                    show_banner("HOMERUN!", color="#ffd700")
                else:
                    show_banner("FOUL!", color="#ff3b30")

        # remove the ball if it flies off screen (cleanup)
        if (abs(x) > SCREEN_W/2 + 80) or (abs(y) > SCREEN_H/2 + 80):
            turt.hideturtle()
            balls.remove(b)

    scr.update()                                    # draw this frame
    scr.ontimer(_tick, TICK_MS)

    # start pitching + physics loop
# =============================================================================
# start pitching + physics loop
_spawn_ball()
_tick()


scr.update()
T.done()

#Source Chatgpt used for math parts of the code