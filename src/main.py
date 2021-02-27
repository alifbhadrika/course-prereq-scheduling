# February 27 2021, Alif Bhadrika Parikesit

def createGraphfromFile():
    '''
    createGraphfromfile adalahh fungsi parse file kemudian
    merepresentasikan data mata kuliah dari file sebagai
    graf dengan berarah dengan struktur adjacency list
    '''

    inputFile = input("ENTER inputFilename.txt: ")
    print()
    with open('../test/'+inputFile,'r') as file:
        graph = {}
        for line in file:
            line = (line.replace(',','').rstrip('.\n')).split()
            graph[line[0]] = (line[1:])
    return graph

def getStudyPlan(graph, sorted_course, course_per_semester):
    '''
    getStudyPlan melakukan topsort pada graf mata kuliah dan menyeleksi
    apakah mata kuliah dapat diletakkan pada satu semester yang sama
    atau tidak
    '''

    vertex = list(graph.keys())             #list simpul graf
    inDegree = dict.fromkeys(vertex,0)      #dict derajat masuk simpul
    smt = 1
    forbidden_course = []                   #course yang memiliki prasyarat course v
    while len(graph) != 0:
        for v in vertex:
            inDegree[v] = len(graph[v])
            if inDegree[v] == 0:
                vertex.remove(v)
                sorted_course.append(v)

                #cek apakah matkul yang baru masuk sorted_course tidak memiliki prasyarat v
                #apabila iya, maka pisah kedua course tersebut
                #apabila tidak, maka satukan keduanya pada satu semester yang sama
                if v not in forbidden_course:
                    if smt in course_per_semester.keys():
                        course_per_semester[smt].append(v)
                    else:
                        course_per_semester[smt] = [v]
                else:
                    smt += 1
                    course_per_semester[smt] = [v]

                forbidden_course.clear()
                
                #penghapusan sisi keluar dari simpul yang berderajat 0   
                for course,neighbors in graph.items():
                    for neighbor in neighbors:
                        if v == neighbor:
                            forbidden_course.append(course)
                            neighbors.remove(neighbor)

                #penghapusan simpul berderajat masuk 0         
                graph.pop(v, None)
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
    sorted_course = []
    course_per_semester = {}
    course_graph = createGraphfromFile()
    getStudyPlan(course_graph,sorted_course,course_per_semester)
    print("==== Sorted Courses List =====")
    print(sorted_course)
    print()
    print("======= Your Study Plan ======")
    print_solution(course_per_semester)
