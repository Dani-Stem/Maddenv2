import pygame, sys
from pygame.sprite import Sprite
from pygame.rect import Rect

WINDOW_WIDTH, WINDOW_HEIGHT = 1368, 712

HIGHLIGHT = "green"

end_item = ["Play Again", "Quit"]


def render_end_menu(winner, screen, selected_index):
    screen.fill("black")

    # Fonts
    end_font = pygame.font.Font("madden25_imgs/font.ttf", 150)
    select_font = pygame.font.Font("madden25_imgs/font.ttf", 100)
    select_font2 = pygame.font.Font("madden25_imgs/font.ttf", 75)

    # Result Message
    if not winner:
        result_text = "YOU LOSE"
        result_color = "red"
    else:
        result_text = "YOU WIN"
        result_color = "green"

    # Render result text
    result_surface = end_font.render(result_text, True, result_color)
    result_rect = result_surface.get_rect(
        midtop=(WINDOW_WIDTH // 2, WINDOW_HEIGHT / 10)
    )
    screen.blit(result_surface, result_rect)

    # Optional subtitle
    if winner:
        quit_surface2 = select_font2.render("Sweet Victory!", True, "yellow")
        quit_rect2 = quit_surface2.get_rect(center=(WINDOW_WIDTH // 2, 225))
        screen.blit(quit_surface2, quit_rect2)

    # Render menu items dynamically
    base_y = WINDOW_HEIGHT / 2 + 10  # Start lower on the screen
    spacing = 120  # Adjust spacing between items
    for index, item in enumerate(end_item):
        text_color = (
            "red"
            if item == "Quit" and index == selected_index
            else HIGHLIGHT if index == selected_index else "white"
        )

        menu_text = select_font.render(item, True, text_color)
        text_rect = menu_text.get_rect(
            center=(WINDOW_WIDTH // 2, base_y + index * spacing)
        )
        screen.blit(menu_text, text_rect)


def end_menu(self, winner):
    self.player_music.stop()
    self.opp_music.stop()

    if not winner:
        self.win_music.stop()
        self.lose_music.play()

    else:
        self.lose_music.stop()
        self.win_music.play()

    self.selected_index = 0

    running = True
    while running:
        render_end_menu(winner, self.screen, self.selected_index)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.highlight_sound.play()
                    self.selected_index = (self.selected_index - 1) % len(end_item)
                elif event.key == pygame.K_DOWN:
                    self.highlight_sound.play()
                    self.selected_index = (self.selected_index + 1) % len(end_item)
                elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    self.confirm_sound.play()
                    if end_item[self.selected_index] == "Quit":
                        pygame.quit()
                        sys.exit()
                    elif end_item[self.selected_index] == "Play Again":
                        reset_game(self)  # Restart the game

        pygame.display.flip()


def reset_game(self):
    self.next_screen = False
    self.outOfBounds = False
    self.outOfBounds2 = False
    self.qbt = True
    self.rbt = False
    self.snap = False
    self.rb_snap = False
    self.caught = False
    self.opps_created = False
    self.stop_opps = None
    self.player_position = (150, 450)
    self.player_touchdown = False
    self.opp_touchdown = False
    self.opp_transition = False
    self.skip = False
    self.next_screen2 = False
    self.new_score = None
    self.rbt_td = False
    self.menu = False
    self.first_render = True  # Add a flag during initialization
    self.first_render2 = True
    self.spacebar_enabled = True

    # Colors
    self.WHITE = (255, 255, 255)
    self.BLACK = (0, 0, 0)
    self.HIGHLIGHT = "green"
    self.start = False

    # Fonts
    self.font = pygame.font.Font("madden25_imgs/font.ttf", 74)  # Default font, size 74

    # Opponent settings
    self.opponents_turn = False
    self.coin_win = False

    # Game data
    self.yardline = [30]
    self.yardline2 = self.yardline[0] + 10
    self.down = 1
    self.yard = 10
    self.score = [0, 0]
    self.white = pygame.Color(255, 255, 255)
    self.playerPos = 1
    self.first = 0
    self.opp_posx = 0
    self.qOutOfBounds = False
    self.opp_down = 1
    self.show_too_far_message = None
    self.opp_sound_paused = False
    self.winner = True
    self.selected_index = 0
    self.down2 = 1
    self.first = 0
    self.music_playing = False
    self.paused = False

    self.coin.unpause()
    self.start_channel.stop()

    self.start_menu()
