from client2server import client2server


class tracker:
    def run(tracklog):
        c2s = client2server()
        i = 0
        while i == 0:
            status = c2s.getStatus()
            dx = int(status) & 0x0fff
            if dx > 2048:
                dx = dx - 4096
            # tracklog.write("Received %d \n" % (dx))
            if abs(int(dx)) < 500:
                if abs(int(dx)) < 10:
                    c2s.moveStop()
                else:
                    if int(dx) > 0:
                        c2s.moveLeft(4)
                    else:
                        c2s.moveRight(4)
        #            return
        c2s.__finit__
