# kHỞI TẠO THƯ VIỆN PYGAME
import pygame
pygame.init()
# VẼ KHUNG CHO TRƯƠNG TRÌNH
screen = pygame.display.set_mode((900,500))
# TẠO MÀU , MÀU ĐC TẠO TỪ CẤC MÀU RGP
RED=(255,0,0)
BLUE=(0,255,255)
BLACK=(0,0,0)
#CÁCH VẼ CHỨ VÀO MÀN HÌNH
#b1 KHỞI TẠO KIỂU CHỮ VÀ CỠ CỮ BẰNG CÂU LẸNH  FONT
font = pygame.font.SysFont('sans', 50)
#B2 GHI VÀO NỘI DUNG CẦN VIẾT BẰNG CÂU LỆNH RENDER
text = font.render("hạnh xinh gái",True,BLACK)
run=True
# ĐỂ VẼ LIÊN TỤC LÊN MÀN HÌNH
while run:
    # DÙNG ĐỂ VẼ KHUNG LIÊN TỤC 
    screen.fill(RED)
    # DÙNG ĐỂ VẼ HÌNH VUÔNG BẰNG CÂU LỆNH RECT
    pygame.draw.rect(screen,BLUE,(10,10,880,480))
    #B3 VẼ LÊN MÀN MÌNH BẰNG CAHS ĐƯA VÀO VÒNG LẶP WHILE VÀ HÀM BLIT
    screen.blit(text,(50,50))
    # TẠO CÁC NÚT TƯƠNG TÁC VỚI TRƯƠNG TRÌNH THEO CẤC CÂU LẸNH 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("hạnh")
    # THAY ĐỔI MÀU CHO TRƯƠNG TRÌNH
    pygame.display.flip()

# TẮT TRƯƠNG TRÌNH KHI KẾT THÚC
pygame.quit()
















