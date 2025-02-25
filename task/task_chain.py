# 任务链
class TaskHandler:
    def __init__(self, func=None):
        self.func = func
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    def handle(self, ip, game_info):
        if self.func:
            self.func(ip, game_info)
        if self.next_handler:
            self.next_handler.handle(ip, game_info)
