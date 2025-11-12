from random import choice, randrange


def make_room(x, y, w, h):
    """
    部屋を表すタプルを返す
    x : 部屋の左上 X 座標
    y : 部屋の左上 Y 座標
    w : 部屋の幅
    h : 部屋の高さ
    """
    return (x, y, w, h)


def room_center(room):
    """
    部屋の中心座標を返す
    room : (x, y, w, h) で表される部屋
    """
    x, y, w, h = room
    return (x + w // 2, y + h // 2)


def is_intersect(a, b):
    """
    2つの部屋 a, b が重なっているか判定
    a : 部屋 a; (x, y, w, h)
    b : 部屋 b; (x, y, w, h)
    """
    ax, ay, aw, ah = a
    bx, by, bw, bh = b
    return not (
        (ax + aw <= bx) or (bx + bw <= ax) or (ay + ah <= by) or (by + bh <= ay)
    )


def carve_room(m, room):
    """
    マップに部屋を作り、マップの二次元リストを返す
    m : 2次元文字列リスト
    room : (x, y, w, h) で表される部屋
    """
    x, y, w, h = room
    return [
        [
            ("." if ((x <= ix < x + w) and (y <= iy < y + h)) else m[iy][ix])
            for ix in range(len(m[0]))
        ]
        for iy in range(len(m))
    ]


def carve_tunnel(m, x1, y1, x2, y2):
    """
    2点間にL字型の通路を掘って、マップの二次元リストを返す
    m : 2次元リスト
    x1, y1 : 通路の開始座標
    x2, y2 : 通路の終了座標
    """
    m = [row[:] for row in m]
    if choice([True, False]):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            m[y1][x] = "."
        for y in range(min(y1, y2), max(y1, y2) + 1):
            m[y][x2] = "."
    else:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            m[y][x1] = "."
        for x in range(min(x1, x2), max(x1, x2) + 1):
            m[y2][x] = "."
    return m


def place_rooms(width, height, max_rooms=30, room_min=5, room_max=12, max_tries=1000):
    """
    マップを初期化し，部屋をランダムに配置し，通路で接続する
    width : マップの幅
    height : マップの高さ
    max_rooms : 最大部屋数
    room_min : 部屋の最小サイズ
    room_max : 部屋の最大サイズ
    max_tries : 配置試行回数の上限
    """
    m = [["#" for _ in range(width)] for _ in range(height)]
    rooms = []
    tries = 0
    while (len(rooms) < max_rooms) and (tries < max_tries):
        w, h = randrange(room_min, room_max + 1), randrange(room_min, room_max + 1)
        x, y = randrange(1, width - w - 1), randrange(1, height - h - 1)
        new_room = make_room(x, y, w, h)
        if all(not is_intersect(new_room, other) for other in rooms):
            m = carve_room(m, new_room)
            if rooms:
                prev_cx, prev_cy = room_center(rooms[-1])
                new_cx, new_cy = room_center(new_room)
                m = carve_tunnel(m, prev_cx, prev_cy, new_cx, new_cy)
            rooms.append(new_room)
        tries += 1
    return m


def generate_dungeon(width=80, height=45, **kwargs):
    """
    ダンジョンマップを生成
    width : マップの幅
    height : マップの高さ
    **kwargs: place_rooms に渡す追加のパラメータ
    """
    return place_rooms(width, height, **kwargs)


def ascii_map(m):
    """
    マップをASCII文字列に変換
    m : 2次元マップ
    """
    return "\n".join("".join(row) for row in m)


if __name__ == "__main__":
    dungeon = generate_dungeon(
        width=40, height=20, max_rooms=4, room_min=1, room_max=10
    )
    print(ascii_map(dungeon))
