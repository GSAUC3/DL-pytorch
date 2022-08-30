import random
'''
- initial population
- cal fitness
- selection
- crossover
- mutation
- new gen
    repeat

'''
TARGET='to be or not to be'


class individual:
    def __init__(self,gene) -> None:
        self.len=len(TARGET)
        self.fitness=0
        self.gene = gene

    def __getitem__(self,i):
        return self.gene[i]
    
    def __repr__(self) -> str:
        return ''.join(self.gene)

DNA = [chr(i) for i in range(32,122)]

def fitness(item):
    global TARGET
    fit = 0
    for i,j in zip(item,TARGET):
        if i==j: fit+=10
        if i in TARGET:fit+=1
    return fit

def selection(p,mr=0.1):
    # global DNA
    new_gen =[]
    for _ in range(90):
        parent1 = random.choice(p[:20])
        parent2 = random.choice(p[:20])
        # crossover
        child = individual([parent1.gene[i] if random.random()<0.5 else parent2.gene[i] for i in range(len(TARGET))])
        # mutation
        child.gene = [random.choice(DNA) if random.random()<mr else i for i in child.gene] 
        new_gen.append(child)
    new_gen.extend(p[:10]) #pass top 10 parents into the next gen
    return new_gen

def main():
    # global DNA
    # create initial population
    Pi = [individual(random.sample(DNA,len(TARGET))) for _ in range(100)]
    b = 1
    print('{:>5} {:^50} {:>5}'.format('Generation','Best Offspring','Fitness'))
    while b:
        # calculate fitnesses of each individual
        fitnesses=list(map(fitness,Pi))
        # store the fitnesses in each individual instance
        for i,x in enumerate(Pi):
            x.fitness = fitnesses[i]
        # sort individuals based on their fitnesses
        Pi = sorted(Pi,key=lambda i:i.fitness,reverse=True)
        # return if correct fitness accquired
        print('{:>5} {:^50} {:>5}'.format(b,str(Pi[0]),Pi[0].fitness))
        if Pi[0].fitness >= len(TARGET)*10 + len(TARGET):
            print('FOUND it 3itch')
            break
        new_gen = selection(Pi) # start selection process
        Pi = new_gen
        b+=1
        if b>999:break
main()

