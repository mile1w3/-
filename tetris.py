import pygame
import random

# 초기화 및 설정
pygame.init()
CELL_SIZE = 30
COLS = 10
ROWS = 20
SCREEN_WIDTH = CELL_SIZE * (COLS + 6)  # 점수판 공간 확보
SCREEN_HEIGHT = CELL_SIZE * ROWS

# 색상 정의 (R, G, B)
COLORS = [
    (0, 0, 0),        # 빈 칸
    (0, 255, 255),    # I 블록 (하늘색)
    (255, 255, 0),    # O 블록 (노란색)
    (128, 0, 128),    # T 블록 (보라색)
    (0, 255, 0),      # S 블록 (초록색)
    (255, 0, 0),      # Z 블록 (빨간색)
    (0, 0, 255),      # J 블록 (파란색)
    (255, 165, 0)     # L 블록 (주황색)
]

# 테트로미노 모양 정의 (4x4 또는 3x3 행렬 형태)
SHAPES = [
    [[1, 1, 1, 1]], # I
    [[2, 2], [2, 2]], # O
    [[0, 3, 0], [3, 3, 3]], # T
    [[0, 4, 4], [4, 4, 0]], # S
    [[5, 5, 0], [0, 5, 5]], # Z
    [[6, 0, 0], [6, 6, 6]], # J
    [[0, 0, 7], [7, 7, 7]]  # L
]

class Tetris:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("파이썬 테트리스")
        self.clock = pygame.time.Clock()
        self.grid = [[0] * COLS for _ in range(ROWS)]
        self.game_over = False
        self.score = 0
        
        self.new_piece()

    def new_piece(self):
        self.current_shape = random.choice(SHAPES)
        self.current_color = SHAPES.index(self.current_shape) + 1
        # 블록 시작 위치 (중앙 상단)
        self.piece_x = COLS // 2 - len(self.current_shape[0]) // 2
        self.piece_y = 0

        if self.check_collision(self.piece_x, self.piece_y, self.current_shape):
            self.game_over = True

    def check_collision(self, nx, ny, shape):
        for r, row in enumerate(shape):
            for c, cell in enumerate(row):
                if cell:
                    if (nx + c < 0 or nx + c >= COLS or 
                        ny + r >= ROWS or 
                        (ny + r >= 0 and self.grid[ny + r][nx + c])):
                        return True
        return False

    def freeze(self):
        for r, row in enumerate(self.current_shape):
            for c, cell in enumerate(row):
                if cell:
                    self.grid[self.piece_y + r][self.piece_x + c] = self.current_color
        self.clear_lines()
        self.new_piece()

    def clear_lines(self):
        lines_to_clear = [i for i, row in enumerate(self.grid) if all(row)]
        for i in lines_to_clear:
            del self.grid[i]
            self.grid.insert(0, [0] * COLS)
        
        # 스코어 계산 (1줄: 100, 2줄: 300, 3줄: 600, 4줄: 1000)
        if len(lines_to_clear) == 1: self.score += 100
        elif len(lines_to_clear) == 2: self.score += 300
        elif len(lines_to_clear) == 3: self.score += 600
        elif len(lines_to_clear) == 4: self.score += 1000

    def rotate(self):
        # 2차원 리스트 시계방향 회전
        rotated = [list(x) for x in zip(*self.current_shape[::-1])]
        if not self.check_collision(self.piece_x, self.piece_y, rotated):
            self.current_shape = rotated

    def move(self, dx):
        if not self.check_collision(self.piece_x + dx, self.piece_y, self.current_shape):
            self.piece_x += dx

    def drop(self):
        if not self.check_collision(self.piece_x, self.piece_y + 1, self.current_shape):
            self.piece_y += 1
        else:
            self.freeze()

    def draw(self):
        self.screen.fill((30, 30, 30))  # 배경 어두운 회색

        # 쌓인 블록 그리기
        for r in range(ROWS):
            for c in range(COLS):
                if self.grid[r][c]:
                    pygame.draw.rect(self.screen, COLORS[self.grid[r][c]], 
                                     (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1))

        # 현재 떨어지는 블록 그리기
        if not self.game_over:
            for r, row in enumerate(self.current_shape):
                for c, cell in enumerate(row):
                    if cell:
                        pygame.draw.rect(self.screen, COLORS[self.current_color], 
                                         ((self.piece_x + c) * CELL_SIZE, (self.piece_y + r) * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1))

        # 게임 구획선 (오른쪽 인터페이스 분리)
        pygame.draw.line(self.screen, (100, 100, 100), (COLS * CELL_SIZE, 0), (COLS * CELL_SIZE, SCREEN_HEIGHT), 2)

        # 점수판 및 안내 텍스트
        font = pygame.font.SysFont("malgungothic", 24) # 윈도우 맑은고딕 기본 적용
        score_txt = font.render(f"SCORE", True, (255, 255, 255))
        score_val = font.render(f"{self.score}", True, (0, 255, 0))
        self.screen.blit(score_txt, (COLS * CELL_SIZE + 20, 30))
        self.screen.blit(score_val, (COLS * CELL_SIZE + 20, 60))

        if self.game_over:
            go_font = pygame.font.SysFont("malgungothic", 40, bold=True)
            go_txt = go_font.render("GAME OVER", True, (255, 0, 0))
            self.screen.blit(go_txt, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2 - 20))

        pygame.display.flip()

    def run(self):
        fall_time = 0
        fall_speed = 500  # 블록이 떨어지는 속도 (ms 단위, 작을수록 빠름)

        while not self.game_over:
            fall_time += self.clock.get_rawtime()
            self.clock.tick()

            # 시간 경과에 따른 자동 하강
            if fall_time >= fall_speed:
                self.drop()
                fall_time = 0

            # 이벤트 처리
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.move(-1)
                    elif event.key == pygame.K_RIGHT:
                        self.move(1)
                    elif event.key == pygame.K_DOWN:
                        self.drop()
                    elif event.key == pygame.K_UP:
                        self.rotate()
                    elif event.key == pygame.K_SPACE:  # 하드 드롭 (바닥으로 한 번에 떨어지기)
                        while not self.check_collision(self.piece_x, self.piece_y + 1, self.current_shape):
                            self.piece_y += 1
                        self.freeze()

            self.draw()

        # 게임 오버 상태 유지 (창을 바로 닫지 않고 대기)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                    return
            self.draw()

if __name__ == "__main__":
    game = Tetris()
    game.run()
    pygame.quit()