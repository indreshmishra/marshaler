import json

class CommonObject:

    def load_deep_json(self, j):
        '''
        This loads object to two level.
        ie. If User Entity contains Address Entity object ,
        __init__ of User Entity should contain same name of parameter as the
        field of Job Entity
        :param j: is json string
        :return:


        '''
        ann = self.__class__.__init__.__annotations__

        self.__dict__.update(json.loads(j))
        for i in self.__dict__.keys():
            v = self.__dict__.get(i)
            if v is not None:
                if type(v)==dict:
                    t = ann.get(i)
                    if t is not None:
                        c = t()
                        c.__dict__.update(v)
                        self.__dict__[i]= c

