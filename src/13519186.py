'''
February 27 2021, Alif Bhadrika Parikesit
Revisi 1
'''

def createGraphfromFile(inputFile):
    '''
    createGraphfromfile adalahh fungsi parse file kemudian
    merepresentasikan data mata kuliah dari file sebagai
    graf dengan berarah dengan struktur adjacency list
    '''

    with open('../test/'+inputFile,'r') as file:
        graph = {}
        for line in file:
            line = (line.replace(',','').rstrip('.\n')).split()
            graph[line[0]] = (line[1:])
    return graph

def inDeg(graph):
    vertex = list(graph.keys())
    inDegree = dict.fromkeys(vertex,0)
    for v in vertex:
        inDegree[v] = len(graph[v])
    return inDegree

def getStudyPlan(graph, sorted_course, course_per_semester):
    '''
    getStudyPlan melakukan topsort pada graf mata kuliah dan menyeleksi
    apakah mata kuliah dapat diletakkan pada satu semester yang sama
    atau tidak
    '''

    smt = 1
    same_semester = []              # list course pada satu semester
    while len(graph) != 0:
        vertex = list(graph.keys()) # list simpul graf
        inDegree = inDeg(graph)     # dict derajat masuk tiap simpul graf
        same_semester.clear()
        for v in vertex:
            if inDegree[v] == 0:
                sorted_course.append(v)

                # seleksi apakah boleh matkul v pada semester smt
                # jika sudah ada 1 atau lebih matkul pada semester smt
                # maka v ditempatkan pada semester yang sama
                if len(same_semester) != 0:
                    course_per_semester[smt].append(v)
                else:
                    course_per_semester[smt] = [v]

                #penghapusan sisi keluar dari simpul yang berderajat 0   
                for course,neighbors in graph.items():
                    for neighbor in neighbors:
                        if v == neighbor:
                            neighbors.remove(neighbor)

                #penghapusan simpul berderajat masuk 0
                graph.pop(v, None)

                #penambahan v pada semester smt
                same_semester.append(v)               
        smt += 1
    return

def print_solution(course_per_semester):
    '''
    print_solution mencetak solusi ke layar sesuai dengan
    format SEMESTER : <nama_course> tiap semesternya
    '''

    for semester,courses in course_per_semester.items():
        print("SEMESTER {}: ".format(semester),end="")
        for course in courses:
            print(course," ",end="")
        print()

if __name__ == '__main__':
    inputFile = input("ENTER inputFilename.txt: ")
    print()

    sorted_course = []
    course_per_semester = {}
    course_graph = createGraphfromFile(inputFile)
    getStudyPlan(course_graph,sorted_course,course_per_semester)
    print("==== Sorted Courses List =====")
    print(sorted_course)
    print()
    print("======= Your Study Plan ======")
    print_solution(course_per_semester)
