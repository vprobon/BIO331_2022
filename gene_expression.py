"""
This Python module provides classes that enable implementing  
a simplified system to model a gene expression study investigating 
candidate disease biomarkers.

The system models:

    - Genes
    - Proteins encoded by genes
    - Experiments measuring gene expression
    - A Study that manages everything
"""

class Gene:
    def __init__(self, gene_id, species, sequence):
        self.gene_id = gene_id
        self.species = species
        self.sequence = sequence.upper()
        self.expression_values = []

    def add_expression(self, value):
        if value < 0:
            raise ValueError("Expression value cannot be negative.")
        self.expression_values.append(value)

    def average_expression(self):
        if not self.expression_values:
            return 0
        return sum(self.expression_values) / len(self.expression_values)

    def gc_content(self):
        g = self.sequence.count("G")
        c = self.sequence.count("C")
        return (g + c) / len(self.sequence) * 100

    def __str__(self):
        return (f"Gene: {self.gene_id} ({self.species})\n"
                f"Length: {len(self.sequence)} bp\n"
                f"Average expression: {self.average_expression():.2f}\n"
                f"GC content: {self.gc_content():.2f}%")
                
                


class Protein:
    def __init__(self, protein_id, sequence, gene):
        self.protein_id = protein_id
        self.sequence = sequence.upper()
        self.gene = gene  # Gene object

    def length(self):
        return len(self.sequence)

    def molecular_weight(self):
        return self.length() * 110  # approximate Da

    def __str__(self):
        return (f"Protein: {self.protein_id}\n"
                f"Encoded by: {self.gene.gene_id}\n"
                f"Length: {self.length()} aa\n"
                f"Approx. MW: {self.molecular_weight()} Da")
                

class Experiment:
    def __init__(self, name, condition):
        self.name = name
        self.condition = condition
        self.genes_measured = []

    def add_gene(self, gene):
        self.genes_measured.append(gene)

    def differential_expression(self, threshold):
        return [gene for gene in self.genes_measured
                if gene.average_expression() > threshold]

    def __str__(self):
        return (f"Experiment: {self.name}\n"
                f"Condition: {self.condition}\n"
                f"Genes measured: {len(self.genes_measured)}")
                

class Study:
    def __init__(self, title):
        self.title = title
        self.genes = []
        self.proteins = []
        self.experiments = []

    def add_gene(self, gene):
        self.genes.append(gene)

    def add_protein(self, protein):
        self.proteins.append(protein)

    def add_experiment(self, experiment):
        self.experiments.append(experiment)

    def summary(self):
        print(f"\nStudy: {self.title}")
        print(f"Total genes: {len(self.genes)}")
        print(f"Total proteins: {len(self.proteins)}")
        print(f"Total experiments: {len(self.experiments)}")