## Genetic Algorithm

Steps:

Repeat until best fitness not found {
- initial population
- calculate fitness
- selection
- crossover
- mutation
- new gen
- initial population = new gen

}

### 1. Initialize population

```python
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


Pi = [individual(random.sample(DNA,len(TARGET))) for _ in range(100)]

```

### 2. Calculate fitness

```python


def fitness(item):
    global TARGET
    fit = 0
    for i,j in zip(item,TARGET):
        if i==j: fit+=10
        if i in TARGET:fit+=1
    return fit

fitnesses=list(map(fitness,Pi))

```

### 3. Selection

```python

def selection(p,mr=0.1):
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
```

### 4. Crossover

Choose any two individuals from the selection population and use crossover method to produce an offspring. 

If the `random.random()` function produces a value greater than **0.5** then take the gene from mother (parent1) else from father (parent2). 

```python
child = individual([parent1.gene[i] if random.random()<0.5 else parent2.gene[i] for i in range(len(TARGET))])
```

### 5. Mutation
Mutation is the random change in the gene which sometime results in a better offspring.

This is done to maintation the diversity in population.
Mutation Rate is denoted by the variable mr, which is set to 0.1
```python
child.gene = [random.choice(DNA) if random.random()<mr else i for i in child.gene] 
```

### 6. New population (generation)
```python
new_gen.extend(p[:10]) #pass top 10 parents into the next gen

new_gen = selection(Pi) # start selection process
Pi = new_gen
```
## output

```
Generation              Best Offspring                    Fitness
------------------------------------------------------------------------
    1                 Y`c1TZv"%nlm &*iF@                    22
    2                 ^*c78:>"Rnli qovDS                    33
    3                 WZ[b%/ :xn0@ mou"@                    45
    4                 7Pcbfkcj%n'd qoYbe                    66
    5                 m@Tbi orUn87 KSiAe                    77
    6                 to ben ]InOj m",QF                    79
    7                 to beZonJ!oj q\$be                   111
    8                 m@ be onJ!oj Zo-be                   111
    9                 t@ be onxno8 Z9nbe                   123
   10                 moXbe orxno8 t9+be                   132
   11                 to be orxno` t9+be                   154
   12                 toXbe orxnoj to$be                   154
   13                 toXbe orxnoj to$be                   154
   14                 to be orxno8 tonbe                   166
   15                 to be orxnoj toobe                   166
   16                 to be orxno8 tonbe                   166
   17                 to be orxno8 tonbe                   166
   18                 to be orxnoj toobe                   166
   19                 to be orxno8 tonbe                   166
   20                 to be orxno` toobe                   166
   21                 to be orAnoj toobe                   166
   22                 to be orino3 tonbe                   166
   23                 to be orxno3 tonbe                   166
   24                 t; be or nop toebe                   166
   25                 to be or no3 tonbe                   177
   26                 to be or no3 tonbe                   177
   27                 to be or noq tonbe                   177
   28                 to be or noC tonbe                   177
   29                 to be or noC tonbe                   177
   30                 to be or no8 tonbe                   177
   31                 to be or no8 tonbe                   177
   32                 to be or no, tonbe                   177
   33                 to be or noH toobe                   177
   34                 to be or no- toobe                   177
   35                 to be or noo toobe                   178
   36                 to be or noo toobe                   178
   37                 to be or noo toobe                   178
   38                 to be or noo toobe                   178
   39                 to be or noo toobe                   178
   40                 to be or noo tobbe                   178
   41                 to be or noo toobe                   178
   42                 to be or noo toobe                   178
   43                 to be or noo toobe                   178
   44                 to be or noo toobe                   178
   45                 to be or noo toobe                   178
   46                 to be or noo tobbe                   178
   47                 to be or noo toobe                   178
   48                 to be or noo toobe                   178
   49                 to be or noo toobe                   178
   50                 to be or noo toobe                   178
   51                 to be or noo tobbe                   178
   52                 to be or noo tobbe                   178
   53                 to be or noo tobbe                   178
   54                 to be or noo tobbe                   178
   55                 to be or noo tobbe                   178
   56                 to be or noo tobbe                   178
   57                 to be or noo toobe                   178
   58                 to be or noo tobbe                   178
   59                 to be or noo toobe                   178
   60                 to be or noo toobe                   178
   61                 to be or noo torbe                   178
   62                 to be or noo toobe                   178
   63                 to be or noo toobe                   178
   64                 to be or noo toobe                   178
   65                 to be or noo toobe                   178
   66                 to be or noo torbe                   178
   67                 to be or noo tobbe                   178
   68                 to be or noo torbe                   178
   69                 to be or noo tobbe                   178
   70                 to be or noo torbe                   178
   71                 to be or noo tobbe                   178
   72                 to be or noo tobbe                   178
   73                 to be or noo tobbe                   178
   74                 to be or noo tobbe                   178
   75                 to be or noo tobbe                   178
   76                 to be or noo torbe                   178
   77                 to be or noo tobbe                   178
   78                 to be or noo tobbe                   178
   79                 to be or noo torbe                   178
   80                 to be or noo tobbe                   178
   81                 to be or noo tobbe                   178
   82                 to be or nob tobbe                   178
   83                 to be or noo torbe                   178
   84                 to be or noo torbe                   178
   85                 to be or noo tobbe                   178
   86                 to be or noo tobbe                   178
   87                 to be or noo tobbe                   178
   88                 to be or noo tobbe                   178
   89                 to be or noo tobbe                   178
   90                 to be or noo tobbe                   178
   91                 to be or noo torbe                   178
   92                 to be or noo tobbe                   178
   93                 to be or noo tobbe                   178
   94                 to be or non torbe                   178
   95                 to be or noo tobbe                   178
   96                 to be or noo tobbe                   178
   97                 to be or noo tobbe                   178
   98                 to be or non tobbe                   178
   99                 to be or non tobbe                   178
  100                 to be or noo tobbe                   178
  101                 to be or non tobbe                   178
  102                 to be or noo tobbe                   178
  103                 to be or not tobbe                   188
  104                 to be or not tobbe                   188
  105                 to be or not tobbe                   188
  106                 to be or not tobbe                   188
  107                 to be or not tobbe                   188
  108                 to be or not to be                   198
```