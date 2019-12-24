class Subject(object):
    def __init__(self):
        self._observers = []  # 观察者列表

    # 注册功能
    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    # 删除功能
    def delete(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    # 通知功能
    def notify(self):
        for observer in self._observers:
            observer.update(self)


# 被观察者数据来源
class Data(Subject):
    def __init__(self, name=''):
        Subject.__init__(self)
        self.name = name
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()


# 观察者
class Viewer:
    def __init__(self, name=''):
        self._name = name

    def update(self, subject):
        print('my name is ', self._name, 'and', subject.name, '***', subject.data)


if __name__ == '__main__':
    data1 = Data('管理员T')
    view1 = Viewer('甲')
    data1.attach(view1)
    view2 = Viewer('乙')
    data1.attach(view2)
    view3 = Viewer('丙')
    data1.attach(view3)

    print('data1初始值')
    print(data1.data)
    print('改变data1的值')
    data1.data = 5
    print('再次改变data1的值')
    data1.data = 10

    print('删除view3后')
    data1.delete(view3)
    data1.data = 90
