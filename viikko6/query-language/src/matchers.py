class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True

class Or:
    def __init__(self,*matchers):
        self._matchers = matchers
        print(self._matchers)

    def test(self,player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True
        return False


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self,player):
        player_value = getattr(player, self._attr)
        return player_value < self._value

class Not:
    def __init__(self, object):
        self._object = object
    
    def test(self,player):
        if self._object.test(player) == True:
            return False
        return True

class All:
    def __init__(self):
        pass
    
    def test(self,player):
        return True

class QueryBuilder:
    def __init__(self, object = All()):
        self._objects = object
    
    def build(self):
        return self._objects

    def playsIn(self, team):
        return QueryBuilder(And(self._objects,PlaysIn(team)))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._objects,HasAtLeast(value,attr)))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._objects,HasFewerThan(value,attr)))

    def oneOf(self, query1, query2):
        return QueryBuilder(Or(query1,query2))