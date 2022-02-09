
from py2neo import Graph,Node,Relationship
from flask import Flask,render_template,request,g,Response
app = Flask(__name__)
url="neo4j+s://e3ec660d.databases.neo4j.io"
pwd="Bot6OCamg2jVh7kHzjulC-6zIWLjKTK6SyAcuUj40zw"
graph=Graph(url,auth=('neo4j',pwd))
query="match (m:Month)-[:VERTICAL]-(v:Vertical)-[:ACCOUNT]-(a:Account)-[:OPPORTUNITY_ID]-(oi:Opportunity_ID) return distinct(v.name) as ver, a.name as acc, m.name as m"

query2="match (v:Vertical) return distinct(v.name) as v"



@app.route("/")
def home():
    res=graph.query(query).data()  
    data=[x for x in res]
    res2=graph.query(query2).data() 
    data2=[x for x in res2] 
    return render_template('index.html',data=data,vk=data2)

@app.route("/q1",methods=["GET","POST"])
def qq():
    if request.method == "POST":
        v=request.form['vertical']
        a=request.form['account']
        res=graph.query(query).data()  
        data=[x for x in res]
        res2=graph.query(query2).data() 
        data2=[x for x in res2] 
       
     
        m=request.form['month']
        print(a)

        if len(m)==3:
            query1="match (m:Month)-[:VERTICAL]-(v:Vertical)-[:ACCOUNT]-(a:Account)-[:OPPORTUNITY_ID]-(oi:Opportunity_ID)-[:OPPORTUNITY_NAME]-(on:Opportunity_Name)-[:OBSERVATION]-(o:Observation)-[:IS_RISKY]-(r:Risky),\
            (b:Billing_Type)-[:BILLING]-(on:Opportunity_Name)-[:DELIVERABLE]-(d:Deliverable_Type),\
            (ot:Observation_Type)-[:OBSERVATION_TYPE]-(o:Observation)-[:STATUS]-(s:Status),\
            (on:Opportunity_Name)-[:DA_APPROVAL]-(da:DA_Approval_Status)\
            \
            return v.name as v,oi.name as oi,on.name as on,o.name as o,b.name as b,d.name as d,s.name as s,ot.name as ot,a.name as a,r.name as r,da.name as da"
            res5=graph.query(query1).data()
            queryfreq="match (m:Month)-[:VERTICAL]-(v:Vertical)-[:ACCOUNT]-(a:Account)-[:OPPORTUNITY_ID]-(oi:Opportunity_ID)-[:OPPORTUNITY_NAME]-(on:Opportunity_Name)-[:OBSERVATION]-(o:Observation)-[:IS_RISKY]-(r:Risky{name:'TRUE'}),\
            (b:Billing_Type)-[:BILLING]-(on:Opportunity_Name)-[:DELIVERABLE]-(d:Deliverable_Type),\
            (ot:Observation_Type)-[:OBSERVATION_TYPE]-(o:Observation)-[:STATUS]-(s:Status),\
            (on:Opportunity_Name)-[:DA_APPROVAL]-(da:DA_Approval_Status)\
            \
            with ot.name as na,count(ot.name) as co\
            where co>2\
            return count(na) as na"
            resfreq1=graph.query(queryfreq).data()

            queryfreqrisk="match (m:Month)-[:VERTICAL]-(v:Vertical)-[:ACCOUNT]-(a:Account)-[:OPPORTUNITY_ID]-(oi:Opportunity_ID)-[:OPPORTUNITY_NAME]-(on:Opportunity_Name)-[:OBSERVATION]-(o:Observation)-[:IS_RISKY]-(r:Risky{name:'TRUE'}),\
            (b:Billing_Type)-[:BILLING]-(on:Opportunity_Name)-[:DELIVERABLE]-(d:Deliverable_Type),\
            (ot:Observation_Type)-[:OBSERVATION_TYPE]-(o:Observation)-[:STATUS]-(s:Status),\
            (on:Opportunity_Name)-[:DA_APPROVAL]-(da:DA_Approval_Status)\
            \
            with ot.name as na,count(ot.name) as co\
            where co>1\
            return count(na) as na"
            resfreqrisk=graph.query(queryfreqrisk).data()


            queryrisky="match (m:Month)-[:VERTICAL]-(v:Vertical)-[:ACCOUNT]-(a:Account)-[:OPPORTUNITY_ID]-(oi:Opportunity_ID)-[:OPPORTUNITY_NAME]-(on:Opportunity_Name)-[:OBSERVATION]-(o:Observation)-[:IS_RISKY]-(r:Risky{name:'TRUE'}),\
            (b:Billing_Type)-[:BILLING]-(on:Opportunity_Name)-[:DELIVERABLE]-(d:Deliverable_Type),\
            (ot:Observation_Type)-[:OBSERVATION_TYPE]-(o:Observation)-[:STATUS]-(s:Status),\
            (on:Opportunity_Name)-[:DA_APPROVAL]-(da:DA_Approval_Status)\
            \
            with count((o.name)) as na\
            return na"
            resrisky=graph.query(queryrisky).data()

            queryriskyopen="match (m:Month)-[:VERTICAL]-(v:Vertical)-[:ACCOUNT]-(a:Account)-[:OPPORTUNITY_ID]-(oi:Opportunity_ID)-[:OPPORTUNITY_NAME]-(on:Opportunity_Name)-[:OBSERVATION]-(o:Observation)-[:IS_RISKY]-(r:Risky{name:'TRUE'}),\
            (b:Billing_Type)-[:BILLING]-(on:Opportunity_Name)-[:DELIVERABLE]-(d:Deliverable_Type),\
            (ot:Observation_Type)-[:OBSERVATION_TYPE]-(o:Observation)-[:STATUS]-(s:Status{name:'Open'}),\
            (on:Opportunity_Name)-[:DA_APPROVAL]-(da:DA_Approval_Status)\
            \
            with count((o.name)) as na\
            return na"
            resriskyopen=graph.query(queryriskyopen).data()

            queryopen="match (m:Month)-[:VERTICAL]-(v:Vertical)-[:ACCOUNT]-(a:Account)-[:OPPORTUNITY_ID]-(oi:Opportunity_ID)-[:OPPORTUNITY_NAME]-(on:Opportunity_Name)-[:OBSERVATION]-(o:Observation)-[:IS_RISKY]-(r:Risky),\
            (b:Billing_Type)-[:BILLING]-(on:Opportunity_Name)-[:DELIVERABLE]-(d:Deliverable_Type),\
            (ot:Observation_Type)-[:OBSERVATION_TYPE]-(o:Observation)-[:STATUS]-(s:Status{name:'Open'}),\
            (on:Opportunity_Name)-[:DA_APPROVAL]-(da:DA_Approval_Status)\
            \
            with count((o.name)) as na\
            return na"
            resopen=graph.query(queryopen).data()

            queryclosed="match (m:Month)-[:VERTICAL]-(v:Vertical)-[:ACCOUNT]-(a:Account)-[:OPPORTUNITY_ID]-(oi:Opportunity_ID)-[:OPPORTUNITY_NAME]-(on:Opportunity_Name)-[:OBSERVATION]-(o:Observation)-[:IS_RISKY]-(r:Risky),\
            (b:Billing_Type)-[:BILLING]-(on:Opportunity_Name)-[:DELIVERABLE]-(d:Deliverable_Type),\
            (ot:Observation_Type)-[:OBSERVATION_TYPE]-(o:Observation)-[:STATUS]-(s:Status{name:'Closed'}),\
            (on:Opportunity_Name)-[:DA_APPROVAL]-(da:DA_Approval_Status)\
            \
            with count((o.name)) as na\
            return na"
            resclosed=graph.query(queryclosed).data()
            
            
            c_5=len(res5)
            queryappr="match (m:Month)-[:VERTICAL]-(v:Vertical)-[:ACCOUNT]-(a:Account)-[:OPPORTUNITY_ID]-(oi:Opportunity_ID)-[:OPPORTUNITY_NAME]-(on:Opportunity_Name)-[:OBSERVATION]-(o:Observation)-[:IS_RISKY]-(r:Risky),\
            (b:Billing_Type)-[:BILLING]-(on:Opportunity_Name)-[:DELIVERABLE]-(d:Deliverable_Type),\
            (ot:Observation_Type)-[:OBSERVATION_TYPE]-(o:Observation)-[:STATUS]-(s:Status),\
            (on:Opportunity_Name)-[:DA_APPROVAL]-(da:DA_Approval_Status{name:'Approved'})\
            \
            return count(distinct(oi.name)) as opn"
            resappr=graph.query(queryappr).data()
            queryappr2="match (m:Month)-[:VERTICAL]-(v:Vertical)-[:ACCOUNT]-(a:Account)-[:OPPORTUNITY_ID]-(oi:Opportunity_ID)-[:OPPORTUNITY_NAME]-(on:Opportunity_Name)-[:OBSERVATION]-(o:Observation)-[:IS_RISKY]-(r:Risky),\
            (b:Billing_Type)-[:BILLING]-(on:Opportunity_Name)-[:DELIVERABLE]-(d:Deliverable_Type),\
            (ot:Observation_Type)-[:OBSERVATION_TYPE]-(o:Observation)-[:STATUS]-(s:Status),\
            (on:Opportunity_Name)-[:DA_APPROVAL]-(da:DA_Approval_Status{name:'Rejected'})\
            \
            return count(distinct(oi.name)) as opn2"
            resappr2=graph.query(queryappr2).data()
            print(resappr2)





        elif v == 'ALL' and len(m)>3:
            query1="match (m:Month)-[:VERTICAL]-(v:Vertical)-[:ACCOUNT]-(a:Account)-[:OPPORTUNITY_ID]-(oi:Opportunity_ID)-[:OPPORTUNITY_NAME]-(on:Opportunity_Name)-[:OBSERVATION]-(o:Observation)-[:IS_RISKY]-(r:Risky),\
            (b:Billing_Type)-[:BILLING]-(on:Opportunity_Name)-[:DELIVERABLE]-(d:Deliverable_Type),\
            (ot:Observation_Type)-[:OBSERVATION_TYPE]-(o:Observation)-[:STATUS]-(s:Status),\
            (on:Opportunity_Name)-[:DA_APPROVAL]-(da:DA_Approval_Status)\
            where m.name='"+m+"'\
            return v.name as v,oi.name as oi,on.name as on,o.name as o,b.name as b,d.name as d,s.name as s,ot.name as ot,a.name as a,r.name as r,da.name as da"
            res5=graph.query(query1).data()
            queryfreq="match (m:Month)-[:VERTICAL]-(v:Vertical)-[:ACCOUNT]-(a:Account)-[:OPPORTUNITY_ID]-(oi:Opportunity_ID)-[:OPPORTUNITY_NAME]-(on:Opportunity_Name)-[:OBSERVATION]-(o:Observation)-[:IS_RISKY]-(r:Risky{name:'TRUE'}),\
            (b:Billing_Type)-[:BILLING]-(on:Opportunity_Name)-[:DELIVERABLE]-(d:Deliverable_Type),\
            (ot:Observation_Type)-[:OBSERVATION_TYPE]-(o:Observation)-[:STATUS]-(s:Status),\
            (on:Opportunity_Name)-[:DA_APPROVAL]-(da:DA_Approval_Status)\
            where m.name='"+m+"'\
            with ot.name as na,count(ot.name) as co\
            where co>2\
            return count(na) as na"
            resfreq1=graph.query(queryfreq).data()

            queryfreqrisk="match (m:Month)-[:VERTICAL]-(v:Vertical)-[:ACCOUNT]-(a:Account)-[:OPPORTUNITY_ID]-(oi:Opportunity_ID)-[:OPPORTUNITY_NAME]-(on:Opportunity_Name)-[:OBSERVATION]-(o:Observation)-[:IS_RISKY]-(r:Risky{name:'TRUE'}),\
            (b:Billing_Type)-[:BILLING]-(on:Opportunity_Name)-[:DELIVERABLE]-(d:Deliverable_Type),\
            (ot:Observation_Type)-[:OBSERVATION_TYPE]-(o:Observation)-[:STATUS]-(s:Status),\
            (on:Opportunity_Name)-[:DA_APPROVAL]-(da:DA_Approval_Status)\
            where m.name='"+m+"'\
            with ot.name as na,count(ot.name) as co\
            where co>1\
            return count(na) as na"
            resfreqrisk=graph.query(queryfreqrisk).data()


            queryrisky="match (m:Month)-[:VERTICAL]-(v:Vertical)-[:ACCOUNT]-(a:Account)-[:OPPORTUNITY_ID]-(oi:Opportunity_ID)-[:OPPORTUNITY_NAME]-(on:Opportunity_Name)-[:OBSERVATION]-(o:Observation)-[:IS_RISKY]-(r:Risky{name:'TRUE'}),\
            (b:Billing_Type)-[:BILLING]-(on:Opportunity_Name)-[:DELIVERABLE]-(d:Deliverable_Type),\
            (ot:Observation_Type)-[:OBSERVATION_TYPE]-(o:Observation)-[:STATUS]-(s:Status),\
            (on:Opportunity_Name)-[:DA_APPROVAL]-(da:DA_Approval_Status)\
            where m.name='"+m+"'\
            with count((o.name)) as na\
            return na"
            resrisky=graph.query(queryrisky).data()

            queryriskyopen="match (m:Month)-[:VERTICAL]-(v:Vertical)-[:ACCOUNT]-(a:Account)-[:OPPORTUNITY_ID]-(oi:Opportunity_ID)-[:OPPORTUNITY_NAME]-(on:Opportunity_Name)-[:OBSERVATION]-(o:Observation)-[:IS_RISKY]-(r:Risky{name:'TRUE'}),\
            (b:Billing_Type)-[:BILLING]-(on:Opportunity_Name)-[:DELIVERABLE]-(d:Deliverable_Type),\
            (ot:Observation_Type)-[:OBSERVATION_TYPE]-(o:Observation)-[:STATUS]-(s:Status{name:'Open'}),\
            (on:Opportunity_Name)-[:DA_APPROVAL]-(da:DA_Approval_Status)\
            where m.name='"+m+"'\
            with count((o.name)) as na\
            return na"
            resriskyopen=graph.query(queryriskyopen).data()

            queryopen="match (m:Month)-[:VERTICAL]-(v:Vertical)-[:ACCOUNT]-(a:Account)-[:OPPORTUNITY_ID]-(oi:Opportunity_ID)-[:OPPORTUNITY_NAME]-(on:Opportunity_Name)-[:OBSERVATION]-(o:Observation)-[:IS_RISKY]-(r:Risky),\
            (b:Billing_Type)-[:BILLING]-(on:Opportunity_Name)-[:DELIVERABLE]-(d:Deliverable_Type),\
            (ot:Observation_Type)-[:OBSERVATION_TYPE]-(o:Observation)-[:STATUS]-(s:Status{name:'Open'}),\
            (on:Opportunity_Name)-[:DA_APPROVAL]-(da:DA_Approval_Status)\
            where m.name='"+m+"'\
            with count((o.name)) as na\
            return na"
            resopen=graph.query(queryopen).data()

            queryclosed="match (m:Month)-[:VERTICAL]-(v:Vertical)-[:ACCOUNT]-(a:Account)-[:OPPORTUNITY_ID]-(oi:Opportunity_ID)-[:OPPORTUNITY_NAME]-(on:Opportunity_Name)-[:OBSERVATION]-(o:Observation)-[:IS_RISKY]-(r:Risky),\
            (b:Billing_Type)-[:BILLING]-(on:Opportunity_Name)-[:DELIVERABLE]-(d:Deliverable_Type),\
            (ot:Observation_Type)-[:OBSERVATION_TYPE]-(o:Observation)-[:STATUS]-(s:Status{name:'Closed'}),\
            (on:Opportunity_Name)-[:DA_APPROVAL]-(da:DA_Approval_Status)\
            where m.name='"+m+"'\
            with count((o.name)) as na\
            return na"
            resclosed=graph.query(queryclosed).data()
            
            
            c_5=len(res5)
            queryappr="match (m:Month)-[:VERTICAL]-(v:Vertical)-[:ACCOUNT]-(a:Account)-[:OPPORTUNITY_ID]-(oi:Opportunity_ID)-[:OPPORTUNITY_NAME]-(on:Opportunity_Name)-[:OBSERVATION]-(o:Observation)-[:IS_RISKY]-(r:Risky),\
            (b:Billing_Type)-[:BILLING]-(on:Opportunity_Name)-[:DELIVERABLE]-(d:Deliverable_Type),\
            (ot:Observation_Type)-[:OBSERVATION_TYPE]-(o:Observation)-[:STATUS]-(s:Status),\
            (on:Opportunity_Name)-[:DA_APPROVAL]-(da:DA_Approval_Status{name:'Approved'})\
            where m.name='"+m+"'\
            return count(distinct(oi.name)) as opn"
            resappr=graph.query(queryappr).data()
            queryappr2="match (m:Month)-[:VERTICAL]-(v:Vertical)-[:ACCOUNT]-(a:Account)-[:OPPORTUNITY_ID]-(oi:Opportunity_ID)-[:OPPORTUNITY_NAME]-(on:Opportunity_Name)-[:OBSERVATION]-(o:Observation)-[:IS_RISKY]-(r:Risky),\
            (b:Billing_Type)-[:BILLING]-(on:Opportunity_Name)-[:DELIVERABLE]-(d:Deliverable_Type),\
            (ot:Observation_Type)-[:OBSERVATION_TYPE]-(o:Observation)-[:STATUS]-(s:Status),\
            (on:Opportunity_Name)-[:DA_APPROVAL]-(da:DA_Approval_Status{name:'Rejected'})\
            where m.name='"+m+"'\
            return count(distinct(oi.name)) as opn2"
            resappr2=graph.query(queryappr2).data()
            print(resappr2)
                
        else:
            query1="match (m:Month)-[:VERTICAL]-(v:Vertical)-[:ACCOUNT]-(a:Account)-[:OPPORTUNITY_ID]-(oi:Opportunity_ID)-[:OPPORTUNITY_NAME]-(on:Opportunity_Name)-[:OBSERVATION]-(o:Observation)-[:IS_RISKY]-(r:Risky),\
            (b:Billing_Type)-[:BILLING]-(on:Opportunity_Name)-[:DELIVERABLE]-(d:Deliverable_Type),\
            (ot:Observation_Type)-[:OBSERVATION_TYPE]-(o:Observation)-[:STATUS]-(s:Status),\
            (on:Opportunity_Name)-[:DA_APPROVAL]-(da:DA_Approval_Status)\
            where v.name='"+v+"' and a.name contains'"+a+"'\
            return v.name as v,oi.name as oi,on.name as on,o.name as o,b.name as b,d.name as d,s.name as s,ot.name as ot,a.name as a,r.name as r,da.name as da"
            res5=graph.query(query1).data()
            queryfreq="match (m:Month)-[:VERTICAL]-(v:Vertical)-[:ACCOUNT]-(a:Account)-[:OPPORTUNITY_ID]-(oi:Opportunity_ID)-[:OPPORTUNITY_NAME]-(on:Opportunity_Name)-[:OBSERVATION]-(o:Observation)-[:IS_RISKY]-(r:Risky{name:'TRUE'}),\
            (b:Billing_Type)-[:BILLING]-(on:Opportunity_Name)-[:DELIVERABLE]-(d:Deliverable_Type),\
            (ot:Observation_Type)-[:OBSERVATION_TYPE]-(o:Observation)-[:STATUS]-(s:Status),\
            (on:Opportunity_Name)-[:DA_APPROVAL]-(da:DA_Approval_Status)\
            where v.name='"+v+"' and a.name contains'"+a+"'\
            with ot.name as na,count(ot.name) as co\
            where co>2\
            return count(na) as na"
            resfreq1=graph.query(queryfreq).data()

            queryfreqrisk="match (m:Month)-[:VERTICAL]-(v:Vertical)-[:ACCOUNT]-(a:Account)-[:OPPORTUNITY_ID]-(oi:Opportunity_ID)-[:OPPORTUNITY_NAME]-(on:Opportunity_Name)-[:OBSERVATION]-(o:Observation)-[:IS_RISKY]-(r:Risky{name:'TRUE'}),\
            (b:Billing_Type)-[:BILLING]-(on:Opportunity_Name)-[:DELIVERABLE]-(d:Deliverable_Type),\
            (ot:Observation_Type)-[:OBSERVATION_TYPE]-(o:Observation)-[:STATUS]-(s:Status),\
            (on:Opportunity_Name)-[:DA_APPROVAL]-(da:DA_Approval_Status)\
            where v.name='"+v+"' and a.name contains'"+a+"'\
            with ot.name as na,count(ot.name) as co\
            where co>1\
            return count(na) as na"
            resfreqrisk=graph.query(queryfreqrisk).data()


            queryrisky="match (m:Month)-[:VERTICAL]-(v:Vertical)-[:ACCOUNT]-(a:Account)-[:OPPORTUNITY_ID]-(oi:Opportunity_ID)-[:OPPORTUNITY_NAME]-(on:Opportunity_Name)-[:OBSERVATION]-(o:Observation)-[:IS_RISKY]-(r:Risky{name:'TRUE'}),\
            (b:Billing_Type)-[:BILLING]-(on:Opportunity_Name)-[:DELIVERABLE]-(d:Deliverable_Type),\
            (ot:Observation_Type)-[:OBSERVATION_TYPE]-(o:Observation)-[:STATUS]-(s:Status),\
            (on:Opportunity_Name)-[:DA_APPROVAL]-(da:DA_Approval_Status)\
            where v.name='"+v+"' and a.name contains'"+a+"'\
            with count((o.name)) as na\
            return na"
            resrisky=graph.query(queryrisky).data()

            queryriskyopen="match (m:Month)-[:VERTICAL]-(v:Vertical)-[:ACCOUNT]-(a:Account)-[:OPPORTUNITY_ID]-(oi:Opportunity_ID)-[:OPPORTUNITY_NAME]-(on:Opportunity_Name)-[:OBSERVATION]-(o:Observation)-[:IS_RISKY]-(r:Risky{name:'TRUE'}),\
            (b:Billing_Type)-[:BILLING]-(on:Opportunity_Name)-[:DELIVERABLE]-(d:Deliverable_Type),\
            (ot:Observation_Type)-[:OBSERVATION_TYPE]-(o:Observation)-[:STATUS]-(s:Status{name:'Open'}),\
            (on:Opportunity_Name)-[:DA_APPROVAL]-(da:DA_Approval_Status)\
            where v.name='"+v+"' and a.name contains'"+a+"'\
            with count((o.name)) as na\
            return na"
            resriskyopen=graph.query(queryriskyopen).data()

            queryopen="match (m:Month)-[:VERTICAL]-(v:Vertical)-[:ACCOUNT]-(a:Account)-[:OPPORTUNITY_ID]-(oi:Opportunity_ID)-[:OPPORTUNITY_NAME]-(on:Opportunity_Name)-[:OBSERVATION]-(o:Observation)-[:IS_RISKY]-(r:Risky),\
            (b:Billing_Type)-[:BILLING]-(on:Opportunity_Name)-[:DELIVERABLE]-(d:Deliverable_Type),\
            (ot:Observation_Type)-[:OBSERVATION_TYPE]-(o:Observation)-[:STATUS]-(s:Status{name:'Open'}),\
            (on:Opportunity_Name)-[:DA_APPROVAL]-(da:DA_Approval_Status)\
            where v.name='"+v+"' and a.name contains'"+a+"'\
            with count((o.name)) as na\
            return na"
            resopen=graph.query(queryopen).data()

            queryclosed="match (m:Month)-[:VERTICAL]-(v:Vertical)-[:ACCOUNT]-(a:Account)-[:OPPORTUNITY_ID]-(oi:Opportunity_ID)-[:OPPORTUNITY_NAME]-(on:Opportunity_Name)-[:OBSERVATION]-(o:Observation)-[:IS_RISKY]-(r:Risky),\
            (b:Billing_Type)-[:BILLING]-(on:Opportunity_Name)-[:DELIVERABLE]-(d:Deliverable_Type),\
            (ot:Observation_Type)-[:OBSERVATION_TYPE]-(o:Observation)-[:STATUS]-(s:Status{name:'Closed'}),\
            (on:Opportunity_Name)-[:DA_APPROVAL]-(da:DA_Approval_Status)\
            where v.name='"+v+"' and a.name contains'"+a+"'\
            with count((o.name)) as na\
            return na"
            resclosed=graph.query(queryclosed).data()
            
            
            c_5=len(res5)
            queryappr="match (m:Month)-[:VERTICAL]-(v:Vertical)-[:ACCOUNT]-(a:Account)-[:OPPORTUNITY_ID]-(oi:Opportunity_ID)-[:OPPORTUNITY_NAME]-(on:Opportunity_Name)-[:OBSERVATION]-(o:Observation)-[:IS_RISKY]-(r:Risky),\
            (b:Billing_Type)-[:BILLING]-(on:Opportunity_Name)-[:DELIVERABLE]-(d:Deliverable_Type),\
            (ot:Observation_Type)-[:OBSERVATION_TYPE]-(o:Observation)-[:STATUS]-(s:Status),\
            (on:Opportunity_Name)-[:DA_APPROVAL]-(da:DA_Approval_Status{name:'Approved'})\
            where v.name='"+v+"' and a.name contains'"+a+"'\
            return count(distinct(oi.name)) as opn"
            resappr=graph.query(queryappr).data()
            queryappr2="match (m:Month)-[:VERTICAL]-(v:Vertical)-[:ACCOUNT]-(a:Account)-[:OPPORTUNITY_ID]-(oi:Opportunity_ID)-[:OPPORTUNITY_NAME]-(on:Opportunity_Name)-[:OBSERVATION]-(o:Observation)-[:IS_RISKY]-(r:Risky),\
            (b:Billing_Type)-[:BILLING]-(on:Opportunity_Name)-[:DELIVERABLE]-(d:Deliverable_Type),\
            (ot:Observation_Type)-[:OBSERVATION_TYPE]-(o:Observation)-[:STATUS]-(s:Status),\
            (on:Opportunity_Name)-[:DA_APPROVAL]-(da:DA_Approval_Status{name:'Rejected'})\
            where v.name='"+v+"' and a.name contains'"+a+"'\
            return count(distinct(oi.name)) as opn2"
            resappr2=graph.query(queryappr2).data()
            print(resappr2)
                


            
        return render_template('index.html',data=data,a=a,v=v,r3=res5,vk=data2,ver=v,freq=resfreq1,m=m,c_5=c_5,appr=resappr,appr2=resappr2,freqrisk=resfreqrisk,risky=resrisky,openrisky=resriskyopen,openob=resopen,closedob=resclosed)
    



@app.route("/neograph")
def neo_graph():
    return render_template('graph.html')    

   
if __name__=='__main__':
    app.run(debug=True)
