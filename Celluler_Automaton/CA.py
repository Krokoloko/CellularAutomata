class CA:
    def __init__(self,grid,adjecentCells,evolve):
        self.evolve = evolve
        self.neighbours = adjecentCells
        self.oldgen = []
        self.newgen = grid
    
    def nextGen(self):
        self.oldgen = self.newgen
        #setting changes to each cell
        nextgen = self.oldgen
        
        for i,x in enumerate(self.oldgen):
            global neighbour
            neighbour = []
            for n in self.neighbours:
                
                try:
                    neighbour.append(self.oldgen[n+i])
                except:
                    if n+i > len(self.oldgen):
                        neighbour.append(self.oldgen[0])
                    if n+i < 0:
                        neighbour.append(self.oldgen[int(len(self.oldgen))-1])
            nextgen[i] = self.evolve(x,neighbour)
        
        self.newgen = nextgen
        
