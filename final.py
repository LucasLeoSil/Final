def ok():
    print("ok")

def canFinish(numCourses, prerequisites):
    preMap = {i:[] for i in range(numCourses)}
    for crs, pre in prerequisites:
        preMap[crs].append(pre)
        
    visitSet = set()
    def dfs(crs):
        if crs in visitSet:
            return False
        if preMap[crs] == []:
            return True
            
        visitSet.add(crs)
        for pre in preMap[crs]:
            if not dfs(pre): return False
        visitSet.remove(crs)
        preMap[crs] = []
        return True
            
    for crs in range(numCourses):
        if not dfs(crs): return False
    return True


with open('inp6.txt', 'r') as final:
    entradas = final.readlines()

numCourses = int(entradas[0][0:-1])

prep = []
mod = entradas[1:]
for i in mod[0:-1]:
    var = i.split(",")
    a = int(var[0])
    b = int(var[1])
    ap = [a,b]
    prep.append(ap)
i = mod[-1]
var = i.split(",")
a = int(var[0])
b = int(var[1])
ap = [a,b]
prep.append(ap)
question = canFinish(numCourses, prep)
if question == True:
    print("Pode ser Concluido")
else:
    print("Não pode ser Concluido")

