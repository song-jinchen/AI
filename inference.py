import os
import sys
import random
import re



class node:
    def __init__(self):
        self.name = ''
        self.parents=[]
        self.cpt_table=[]
    def __str__(self):
        s = 'name: ' + self.name + '\n'
        s += 'parents: ' + str(self.parents) + '\n'
        s += 'cpt_table' + str(self.cpt_table) + '\n\n\n'
        return s

def read_bayesian_network(graphfile):
    
    with open(graphfile) as f:
        a= f.readline()
        N = int(a)
        f.readline()

        b= f.readline()
        c= b.split()
        Names =c
        f.readline()
        
        Adjacency_table = []
        for i in range(N):
            d= f.readline()
            e=d.split()
            t = e
            t = [int(i) for i in e]
            g=Adjacency_table.append(t)
            g
        f.readline()

       
        Nodes = []
        for i in range(N):
            n = node()
            n.name = Names[i]

            for j in range(N):
                aa=n.parents
                ab =Adjacency_table
                if ab[j][i] == 1:
                    aa.append(Names[j])
           
            for j in range(2**len(aa)):
                ac=f.readline()
                ad=ac.split()
                line = ad
                line = [float(i) for i in ad]
                ae=n.cpt_table.append
                ae(line)
            f.readline()
            Nodes.append(n)

    res = {}
    for i in range(N):
        af= res.update
        af({Names[i]:Nodes[i]})
    return res


def topo_sorting():
    global Nodes
    af =Nodes.values()
    Names = [i.name for i in af]
    for n in Names:        
        ag= Nodes[n].parents
        Nodes[n].entry_num = len(ag)
    
    finsh_num = 0
    res = []
    while finsh_num != len(Nodes):
        for i in Nodes.values():
            if i.entry_num != 0:
                pass
            else:                
                i.entry_num= -1
                finsh_num += 1
                ai= res.append
                ai(i.name)
                ak= Nodes.values()
                for j in ak:
                    al=i.name
                    am=j.parents
                    if al in am:    
                        j.entry_num -= 1
                   
    return res

def p_with_status(node_i, previous_name, previous_status, p_true_false=1):
    an =previous_name
    ao= previous_status
    status_dict = dict(zip(an,ao))
    ap=status_dict
    aq=node_i.parents
    p_index = [ap[i] for i in reversed(aq)]
    ar=p_index
    p_index = sum([value * (2**index) for index,value in enumerate(ar)])
    if p_true_false == 1:
        p_col = 0
    if p_true_false ==0:
        p_col = 1
    au= node_i.cpt_table
    return au[p_index][p_col]


def cal_weight(evidence_status={}):
    global Nodes, sorted_names
   
    status = []
    W = []
    def dfs(sorted_names_last, w, status_i):
        av =sorted_names_last
        aw=status.append
        if len(av) == 0:
            aw(status_i)
            W.append(w)
            return
        name_i = sorted_names_last[0]
        if name_i in evidence_status.keys():
            pass
        else:
            dfs(sorted_names_last[1:], w, status_i + [0])

        if name_i not in evidence_status.keys():
            dfs(sorted_names_last[1:], w, status_i + [1])
        else:
            w *= p_with_status(Nodes[name_i], sorted_names[:len(status_i)], status_i, evidence_status[name_i])
            ay= evidence_status[name_i]
            dfs(sorted_names_last[1:], w, status_i+[ay])

            


    dfs(sorted_names, 1.0, [])
    return status, W

def status_list_to_str_num(status):
    res = []
    for i in status:
     
        num = str(sum([value*(2**index) for index, value in enumerate(i)]))
        
        res.append(num)
    return res


def generate_samples(samples_count=10000, evidence_status={}):
    global Nodes, sorted_names
    samples = []
    az= evidence_status.keys()
    evidence_var = az

    for i in range(samples_count):
        status_i = []
        ba= sorted_names
        bb=status_i.append
        for name in ba:
            if name in evidence_var:
                bb(evidence_status[name])
            else:
                                
                node_i = Nodes[name]
                bc= node_i
                p = p_with_status(bc, sorted_names[:len(status_i)], status_i, 1)
                if name not in evidence_var:
                    true_or_false = random.random() <= p  
                    status_i.append(true_or_false + 0)
        bd=samples.append
        bd(status_i)
    return samples


def generate_p_status(sorted_names, evidence_status={}, query_var={}):
    status = []
    def dfs(sorted_names_last, status_i):
        be =sorted_names_last
        if len(be) == 0:
            status.append(status_i)
            return
        else:
            name_i = sorted_names_last[0]
            if name_i not in evidence_status.keys() and name_i not in query_var.keys():
                dfs(sorted_names_last[1:], status_i + [0])
            if name_i in evidence_status.keys():
                bf= evidence_status
                dfs(sorted_names_last[1:], status_i+[bf[name_i]])
            elif name_i in query_var.keys():
                bg= query_var
                dfs(sorted_names_last[1:], status_i+[bg[name_i]])
            if name_i not in evidence_status.keys():
                if name_i in query_var.keys():
                    pass
                else:
                    dfs(sorted_names_last[1:], status_i + [1])
    dfs(sorted_names, status_i=[])
    return status


def read_query(queryfilepath):
   
    bj=queryfilepath
    with open(bj) as f:
        l = f.readline()
        bi=re.compile
        p = bi("P\((.*?) \|")
        bh=p.findall
        query = bh(l)[0] # query
        query = {query:1}

        bk= re.compile
        pattern = bk(r"\| (.*?)\)")
        bm=pattern.findall
        m = bm(l)[0]
        m = m.replace(' ', '')
        m = m.split(',')

        if type(m) == str:
            m = [m]
        evidence = {}
        for i in m:
            i = i.split('=')
            bl=evidence.update
            if i[1] == 'true':
                bl({i[0]:1})
            if i[1] == 'false':
                bl({i[0]:0})
    bn =query
    return bn, evidence


def cal_p(samples, query_status, status_w_dict):
    bo=status_w_dict
    total_sum = sum(bo[s] for s in samples)
    query_in_sample = []
    query_off_sample = []
    bp=samples
    for i in bp:
        if i in query_status:
            if i in samples:
                query_in_sample.append(i)
        if i not in query_status:
            if i in query_status:
                query_in_sample.append(i)
            else:
                query_off_sample.append(i)
    if i in query_in_sample or i in query_off_sample:
        pos_query_sum = sum(status_w_dict[s] for s in query_in_sample)
        neg_query_sum = sum(status_w_dict[s] for s in query_off_sample)
        # evidence_status =0
        # samples = []
        # evidence_var = evidence_status

        pos = pos_query_sum/total_sum
        neg = neg_query_sum/total_sum
    bq=pos
    return bq, neg

graphfile=sys.argv[1]

querypath=sys.argv[2]



br=read_query(querypath)
query_var, evidence_status = br

bs=read_bayesian_network(graphfile)
Nodes = bs

bt= topo_sorting()
sorted_names = bt

bu=cal_weight(evidence_status=evidence_status)
status, W = bu

bv= dict(zip(status_list_to_str_num(status), W))
status_w_dict =bv

bw= generate_samples(1500000, evidence_status=evidence_status)

samples = bw
samples = status_list_to_str_num(samples)
by=generate_p_status(sorted_names, evidence_status=evidence_status, query_var=query_var)

query_status = by
query_status = status_list_to_str_num(query_status)


t, f = cal_p(samples, query_status, status_w_dict)

print t,f



            





