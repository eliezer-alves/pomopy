from app.Models import Model, Tags, Tasks
from datetime import datetime
SQL_GET_CYCLES_FROM_USER = '''
select
    *
from cycles c
inner join users u on u.id = c.users_id
inner join tags tg on tg.id = c.tags_id
left join tasks tk on tk.id = c.tasks_id
where u.id = {}
'''

class Cycles(Model):
    def __init__(self) -> None:
        super().__init__()
        self.tags = Tags()
        self.tasks = Tasks()
        self.table = 'cycles'
        self.fillable = [
            'duration_in_minutes',
            'status',
            'tags_id',
            'tasks_id',
            'users_id',
            'start',
            'end',
        ]
    
    def getCyclesFromUser(self, userId):
        cycles = self.select().where('users_id', userId)
        cycles.query = cycles.query + " order by id desc"
        cycles = cycles.get()
        returCycles = []
        for cycle in cycles:
            tag = self.tags.find(cycle['tags_id'])
            cycle['tag'] = tag
            if(cycle['tasks_id'] != None):
                task = self.tasks.find(cycle['tasks_id'])
                cycle['task'] = task
                True
            returCycles.append(cycle)
        
        return returCycles
        