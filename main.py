import tcod

from engine import Engine
from entity import Entity
from procgen import generate_dungeon
from input_handlers import EventHandler

def main() -> None:
    # Defining size of screen
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    # Telling tcod what tileset to use
    tileset = tcod.tileset.load_tilesheet(
        "assets\\dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0))
    entities = {player, npc}

    game_map = generate_dungeon(map_width, map_height)

    engine = Engine(entities=entities, event_handler=event_handler, game_map = game_map, player=player)

    #Creating the Screen that is drawn to
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True,
    ) as context:
        # Creating the console to host the screen
        root_console = tcod.Console(screen_width, screen_height, order='F')
        # Main gameloop
        while True:
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()

            engine.handle_events(events)

if __name__ == "__main__":
    main()