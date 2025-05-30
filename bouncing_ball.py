import pygame

# Khởi tạo Pygame
pygame.init()

# Thiết lập màn hình
WIDTH = 800
HEIGHT = 600
BG_COLOR = (255, 255, 255)  # Màu nền trắng
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Game")

# Thiết lập bóng
BALL_RADIUS = 20
BALL_COLOR = (255, 0, 0)  # Màu đỏ cho bóng
ball_pos = [WIDTH // 2, HEIGHT // 2]  # Vị trí ban đầu của bóng (giữa màn hình)
ball_speed = [5, 5]  # Tốc độ di chuyển của bóng theo trục x và y


# Vòng lặp game chính
def main():
    running = True
    while running:
        # Xử lý sự kiện
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Thoát game khi nhấn nút đóng cửa sổ

        # Cập nhật vị trí bóng
        ball_pos[0] += ball_speed[0]
        ball_pos[1] += ball_speed[1]

        # Xử lý va chạm với các cạnh màn hình
        if ball_pos[0] <= BALL_RADIUS or ball_pos[0] >= WIDTH - BALL_RADIUS:
            ball_speed[0] = -ball_speed[0]  # Đảo chiều ngang
            bounce_sound.play()

        if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
            ball_speed[1] = -ball_speed[1]  # Đảo chiều dọc
            bounce_sound.play()

        # Xóa màn hình
        screen.fill(BG_COLOR)

        # Vẽ bóng
        pygame.draw.circle(screen, BALL_COLOR, (int(ball_pos[0]), int(ball_pos[1])), BALL_RADIUS)

        # Cập nhật màn hình
        pygame.display.flip()

        # Điều chỉnh tốc độ khung hình
        pygame.time.Clock().tick(60)


# Tải âm thanh va chạm
bounce_sound = pygame.mixer.Sound("bounce.wav")  # Cần có file âm thanh "bounce.wav" trong thư mục

# Chạy game
if __name__ == "__main__":
    main()

# Thoát Pygame
pygame.quit()