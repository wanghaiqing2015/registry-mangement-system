#coding=utf-8

from functools import wraps
 
def login_required(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        terminal = self.session.get("user", None)
        
        if terminal:
            return func(self, *args, **kwargs)
        else:
            self.redirect(self.reverse_url('login'))
    return wrapper