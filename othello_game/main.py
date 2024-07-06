from . import WIDTH, HEIGHT, CELL_SIZE, ROWS, COLS, BLACK, WHITE, GREEN, GRAY
import pygame
import sys

pygame.init()

# ゲームボードの初期化（0: 空、1: 黒、-1: 白）
board = [[0]*COLS for _ in range(ROWS)]
board[3][3], board[4][4] = 1, 1
board[3][4], board[4][3] = -1, -1

# 画面の設定
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Othello (Reversi)")

# メインループ
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_board()
        pygame.display.flip()

    pygame.quit()
    sys.exit()

# ゲームボードを描画する関数
def draw_board():
    screen.fill(GREEN)
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if board[row][col] == 0 else BLACK if board[row][col] == 1 else GRAY
            pygame.draw.rect(screen, color, (col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, BLACK, (col*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE), 2)

if __name__ == "__main__":
    main()
