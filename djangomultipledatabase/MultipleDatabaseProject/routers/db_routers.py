class AuthRouter:
    router_app_lables={'auth','contenttypes','sessions','admin'}

    def db_for_read(self,model,**hints):
        if model._meta.app_label in self.router_app_lables:
            return 'my_db'
        return None

    
    def db_for_write(self,model,**hints):
        if model._meta.app_label in self.router_app_lables:
            return 'my_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'my_db'
        return None


class MultipleDatabaseApp:
    router_app_lables={'MultipleDatabaseApp'}

    def db_for_read(self,model,**hints):
        if model._meta.app_label in self.router_app_lables:
            return 'MultipleDatabaseApp'
        return None

    
    def db_for_write(self,model,**hints):
        if model._meta.app_label in self.router_app_lables:
            return 'MultipleDatabaseApp'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'MultipleDatabaseApp'
        return None

class Aqua:
    router_app_lables={'Aqua'}

    def db_for_read(self,model,**hints):
        if model._meta.app_label in self.router_app_lables:
            return 'Aqua'
        return None

    
    def db_for_write(self,model,**hints):
        if model._meta.app_label in self.router_app_lables:
            return 'Aqua'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'Aqua'
        return None



    

