from flask import Flask, render_template, request


app = Flask(__name__)

flag = 0
start = {'1' : 0,'2': 0}
aspirant = {'2.1': 0,'2.2': 0}
student = {'1.1': 0,'1.2': 0,'1.3': 0,'1.4': 0,'1.5': 0,'1.6': 0}
p1 = {'1.1.1':0,'1.1.2':0}
p2 = {'1.2.1':0,'1.2.2':0}
e1 = {'1.3.1':0,'1.3.2':0}
e2 = {'1.4.1':0,'1.4.2':0}
e3 = {'1.5.1':0,'1.5.2':0}
e4 = {'1.6.1':0,'1.6.2':0}
p1_others = ['1.1.2.1','1.1.2.2','1.1.2.3','1.1.2.4','1.1.2.5','1.1.2.6','1.1.2.7']
p2_others = ['1.2.2.1','1.2.2.2','1.2.2.3','1.2.2.4','1.2.2.5','1.2.2.6','1.2.2.7']
e1_others = ['1.3.2.1','1.3.2.2','1.3.2.3','1.3.2.4','1.3.2.5','1.3.2.6','1.3.2.7']
e2_others = ['1.4.2.1','1.4.2.2','1.4.2.3','1.4.2.4','1.4.2.5','1.4.2.6','1.4.2.7']
e3_others = ['1.5.2.1','1.5.2.2','1.5.2.3','1.5.2.4','1.5.2.5','1.5.2.6','1.5.2.7']
e4_others = ['1.6.2.1','1.6.2.2','1.6.2.3','1.6.2.4','1.6.2.5','1.6.2.6','1.6.2.7']
p1_academics = {
    "1.1.1.1":"""<b>Sem1 subjects:</b><ul><li>Physics</li><li>Chemistry</li><li>Maths</li><li>English</li><li>Telugu</li><li>IT</li></ul>
    <b>Sem2 subjects:</b><ul><li>Physics</li><li>Chemistry</li><li>Maths</li><li>English</li><li>Telugu</li><li>IT</li></ul>""",
    "1.1.1.2":"""<b>Sem1 faculty:</b><br><ul><li><i>Maths-BhaskarRao</i>,<a href = "mailto:bhaskarrao.betha@gmail.com">bhaskarrao.betha@gmail.com</a></li>
                <li><i>Physics</i>-Raghavendra rao,<a href = "mailto:raghavendraraotammina@gmail.com">raghavendraraotammina@gmail.com</a></li>
                <li><i>Chemistry</i>-BhavanaRishi,<a href = "mailto:rushichem09@gmail.com">rushichem09@gmail.com</a></li>
                <li><i>English</i>-Sekhar,<a href = "mailto:sekhar.yet@rguktsklm.ac.in">sekhar.yet@rguktsklm.ac.in</a></li>
                <li><i>Telugu</i>-prakashrao sir                </li>
                <li><i>IT</i>-S.Sateesh Kumar,<a href = "mailto:sateesh@rguktsklm.ac.in">sateesh@rguktsklm.ac.in</a><br></li></ul>
                <b>Sem2 faculty:</b><ul><li><i>Maths</i>-Gnanedrarao,...</li></ul>""",
    "1.1.1.3":"<a href = 'https://examcell.rguktsklm.ac.in'>Click here for results</a>",
    "1.1.1.4":"""<ul><li>The library opens daily at sharply 9am everyday except for holidays sometimes and will close by 9pm.</li>
                <li>There will be all types of books available along with the newspaper daily.</li>
                <li>You need to enter the book details and your details if you want to bring the book to the hostelrooms.</li>
                </ul>""",
    "1.1.1.5":"<b>Sem1 labs</b>:<ul><li>Physics</li><li>Chemistry</li></ul><b>Sem2 labs</b>:<ul><li>Physics</li><li>Chemistry</li></ul>"
}
others  = {
    "1":"""<ul><li>RGUKT provides facilities for both indoor games such as Carroms and Chess at the pyshical education room.</li><br>
                 <li>And outdoor games such as Volleyball,Cricket,Kabaddi,Basketball and Football facilities are at the sports room and the ground.</li><br>
                 <li>It is anticipated to hold inter-campus competitions will also be held.</li>
                 <li>sports sir:G.Veera babu,<a href = "mailto:veerababug8888@rguktsklm.ac.in">perumalisankar.mfa@rguktsklm.ac.in</a></li></ul>""",
    "2":"""<ul><li>RGUKT goal is to give well-rounded education to the students.</li>
                 <li>Students are encouraged to get involved in arts,music,drama,dance,yoga and other related skills.</li>
                 <li>Art classes will be held at the Beta-4 room.</li>
                 <li>Art sir:P.Siva Senkhar,<a href = "mailto:perumalisankar.mfa@rguktsklm.ac.in">perumalisankar.mfa@rguktsklm.ac.in</a></li>
                 <li>The dance classes will be held at the Beta-8.</li>
                 <li>Dance sir:..............,email-.............</li>
                 <li>The yoga classes are held at the Beta-12</li>
                 <li>Yoga sir:Dhanunjay,email-...........</li>
                 <li>The music classes are held at the Beta-6</li>
                 <li>Music sir:..........,email-.............</li></ul>""",
    "3":"""
    <table>
            <tr>
                <th>Day</th> <th>Breakfast</th> <th>Lunch</th> <th>Snacks</th><th>Dinner</th>
            </tr>
            <tr>
                <td>Monday</td><td>Idly<br>Palli chutney</td><td> Potato fry<br>Sambar<br>Curd</td><td>Senagalu<br>Tea</td><td>Brinjal & Peas curry<br>Chutney</td>
            </tr>
            <tr>
                <td>Tuesday</td><td>Utappam<br>Palli chutney</br></td><td>Cabbage<br>Sambar<br>Curd</td><td>Senagunda<br>Tea</br></td><td>Potato & Carrot curry<br>Curd</br></td>
            </tr>
            <tr>
                <td>Wednesady</td><td>Bonda/Vada<br>Palli chutney</td><td>Drumstick curry<br>Sambar<br>Curd</td><td>Pakodi<br>Tea</td><td>Biryani<br>Chicken,Panner curry</td>
            </tr>
            <tr>
            <td>Thursday</td><td>Upma<br>Palli chutney</td><td> Cluster Beans curry<br>Dal<br>Curd</td><td>Popcorn<br>Tea</td><td>Chapathi<br>Potato curry</td>
            </tr>
            <tr>
                <td>Friday</td><td>Idly<br>Sambar</td><td>Potato &Carrot fry<br>Dal with curry leaves<br>Curd</td><td>Fried peas<br>Tea</td><td>Egg,Carrot curry<br>Curd</br></td>

            </tr>  
            <tr>
                <td>Saturday</td><td>Puri<br>Potato curry</td><td>Cluster Beans &Bundi fry<br>Sambar<br>Curd</td><td>Biscuits<br>Tea</td><td>Pulihora<br>Chutney</td>
            </tr>
            <tr>
                <td>Sunday</td><td>Dosa<br>Palli chutney</td><td>Chicken /Panner curry<br>Rasam<br>Curd</td><td>Boiled Groundnuts<br>Tea</td><td>Kandha gadda curry<br>Curd</td>
            </tr>
            
        </table>
    """,
    "4":"""Mess feedback forms: <ul><li> mess feedback forms will provided by the mail</li><li><a href = "mailto:chiefmesscoordinator@rguktsklm.ac.in">chiefmesscoordinator@rguktsklm.ac.in</a></li>
    <br>Faculty feedback froms:""",
    "5":"""<ul><li>When students want to go out of campus ,parents are required  to come and pick them up.</li>
	<li>No food from outside is allowed in the hostel.</li> 
	<li>Students are not allowed after 10pm to the hostel rooms.</li>
	<li>No ragging is allowed in the campus.</li>
        <li>To behave and conduct themselves in the Institute campus, hostels and premises in a dignified and courteous manner and show due respect to the authorities, employees and elders.</li> 
        <li>To follow decent and formal dressing manners.</li>
	<li>Students should avoid clothing depicting illegal drugs, alcohol, prophane language, racial, sexual and vulgar captions etc.</li> 
        <li>To access all educational opportunities and benefits available at the Institute and make good use of them to prosper academically and develop scientific temper.</li> 
        <li>To respect the laws of the country, human rights and to conduct in a responsible and dignified manner at all times.</li> 
        <li>To report any violation of this Code to the functionaries under this code.</li></ul>""",
    "6":"""<ul><li>RGUKT provides all the necessary medical facilities to it's students at the Hospital.</li>
        <li>Ambulance contact:</li></ul>""",
    "7":"""<ul><li>Parent or Guardian whom you want to take outpass should be in ParentID card</li>
        <li>Apply leave Before 3 days going manually by approaching warden mam.</li>
        <li>When parent or guardian came to the college you need to verify with the details in the parentIDcard</li>
        <li>After verifying details Take outpass from the caretaker.</li>
        <li>And finally show the outpass to the security at the gate.</li></ul>"""

}

p2_academics = {
    "1.2.1.1":"""<b>Sem1 subjects:</b><ul><li>Physics</li><li>Chemistry</li><li>Maths</li><li>English</li><li>Telugu</li><li>IT</li></ul>
    <b>Sem2 subjects:</b><ul><li>Physics</li><li>Chemistry</li><li>Maths</li><li>English</li><li>Telugu</li><li>IT</li></ul>""",
    "1.2.1.2":"""<b>Sem1 faculty:</b><br><ul><li><i>Maths-BhaskarRao</i>,<a href = "mailto:bhaskarrao.betha@gmail.com">bhaskarrao.betha@gmail.com</a></li>
                <li><i>Physics</i>-Raghavendra rao,<a href = "mailto:raghavendraraotammina@gmail.com">raghavendraraotammina@gmail.com</a></li>
                <li><i>Chemistry</i>-BhavanaRishi,<a href = "mailto:rushichem09@gmail.com">rushichem09@gmail.com</a></li>
                <li><i>English</i>-Sekhar,<a href = "mailto:sekhar.yet@rguktsklm.ac.in">sekhar.yet@rguktsklm.ac.in</a></li>
                <li><i>Telugu</i>-                 </li>
                <li><i>IT</i>-S.Sateesh Kumar,<a href = "mailto:sateesh@rguktsklm.ac.in">sateesh@rguktsklm.ac.in</a><br></li></ul>
                <b>Sem2 faculty:</b><ul><li><i>Maths</i>-Gnanedrarao,...</li></ul>""",
    "1.2.1.3":"<a href = 'https://examcell.rguktsklm.ac.in'>Check your results here</a>",
    "1.2.1.4":"""<ul><li>The library opens daily at sharply 9am everyday except for holidays sometimes and will close by 9pm.</li>
                <li>There will be all types of books available along with the newspaper daily.</li>
                <li>You need to enter the book details and your details if you want to bring the book to the hostelrooms.</li>
                </ul>""",
    "1.2.1.5":"<b>Sem1 labs</b>:<ul><li>Physics</li><li>Chemistry</li></ul><b>Sem2 labs</b>:<ul><li>Physics</li><li>Chemistry</li></ul>"
}



e1_academics = {
    "1.3.1.1":"""<b>Sem1 subjects:</b><ul><li>Calculus & Linear Algebra</li><li>Basic Electrical and Electronics Engineering(BEEE)</li><li>Problem Solving and Programming Through C(PSTC)</li><li>Indian Constitution(IC)(credit less subject)</li></ul>
             <b>Sem2 subjects:</b><ul><li>Discrete Mathematics(DM)</li><li>Engineering Physics</li><li>Managerial Economics and Finance Accounting(MEFA)</li><li>Object Oriented Programming through Java(OOPS)</li><li>Data Structures(DS)</li><li>Environmental Sciences(credit less subject)</li></ul>""",
    "1.3.1.2" : """<b>Sem1 faculty:</b><i>Calculus & Linear Algebra</i>-Dr.B.Bhaskar rao,<a href = "mailto:bhaskararao.betha@gmail.com">bhaskararao.betha@gmail.com</a><br>
                <i>BEEE</i>-M Ramu,<a href = "mailto:mullangi.ramu0206@gmail.com">mullangi.ramu0206@gmail.com</a><br>
                <i>PSTC</i>-Mr. S.Sateesh Kumar,<a href = "mailto:sateesh@rguktsklm.ac.in">sateesh@rguktsklm.ac.in</a><br>
                <b>sem2 faculty:</b><br><i>DM</i>-Dr.B.Bhaskar rao,<a href = "mailto:bhaskararao.betha@gmail.com">bhaskararao.betha@gmail.com</a><br>
                <i>Engineering Physics</i>-N Ramesh Babu,<a href = "mailto:ramesh.nuthakki@gmail.com">ramesh.nuthakki@gmail.com</a><br>
                <i>MEFA</i>-outside faculty<br>
                <i>OOPS</i>-Mr. Y.Ramesh,<a href = "mailto:ramesh.yajjala42@rguktsklm.ac.in">ramesh.yajjala42@rguktsklm.ac.in</a><br> 
                <i>DS</i>-Mr. S.Sateesh Kumar,<a href = "mailto:sateesh@rguktsklm.ac.in">sateesh@rguktsklm.ac.in</a>""",
    "1.3.1.3": "<a href = 'https://examcell.rguktsklm.ac.in'>Click here for results</a>",
    "1.3.1.4":"""<ul><li>The library opens daily at sharply 9am everyday except for holidays sometimes and will close by 9pm.</li>
                <li>There will be all types of books available along with the newspaper daily.</li>
                <li>You need to enter the book details and your details if you want to bring the book to the hostelrooms.</li>
                </ul>""",
    "1.3.1.5":"""<b>Sem1 labs</b>:<ul><li>English-Lab-I</li><li>BEEELab</li><li>PSTC Lab</li></ul>
	<b>Sem2 labs</b>:<ul><li>Engineering Physics Lab</li><li>OOPS Lab</li><li>Data Structures Lab</li></ul>""",
    "1.3.1.6":"""<ul><li>The students who are not from the eligible background need to pay the whole money to college.</li>
	<li>They don't get any scholarships.</li><li>The students who are eligible for scholarship need to pay the Vidyadevena,Vasathidevena money for every semester</li></ul>"""
}


e2_academics={
    "1.4.1.1":"""<b>Sem1 subjects</b>:<ul><li>Probability and Statistics(P&S)</li><li>Formal Languages & Automata Theory(FLAT)</li><li>Digital Logic Design(DLD)</li><li>Design & Analysis of Algorithms(DAA)</li><li>Database Management Systems(DBMS)</li></ul>
	<b>Sem2 subjects</b>:<ul><li>Operational Research(OR)</li><li>Computer Organization & Architecture(COA)</li><li>Data Science with Python(DSP)</li><li>Compiler Design(CD)</li><li>Web Technologies(WT)</li></ul>""",
    "1.4.1.2" :"""<b>Sem1 faculty</b>:<br>
	<i>P&S</i>:Dr.B.Bhaskar rao,<a href = "mailto:bhaskararao.betha@gmail.com">bhaskararao.betha@gmail.com</a><br> 
	Mr. Y.Ramesh<br>
	N.Sesha kumar<br>
	Anil Kumar<br>
	N.Rameshbabu <br> 
	<b>Sem2 faculty</b>:<br>
	ch.satish kumar<br>Vishnu priyanka<br>s.sateesh""",
    "1.4.1.3": """<b>Sem1 labs</b>:<ul><li>Design & Analysis of Algorithms Lab</li><li>Digital Logic Design Lab</li><li>Database Management Systems Lab</li></ul>
	<b>Sem2 labs</b>:<ul><li>English Lab-II</li><li>Computer Organization & Architecture Lab</li><li>Data Science with Python Lab</li><li>Web Technologies Lab</li></ul>""",
    "1.4.1.4":"<a href = 'https://examcell.rguktsklm.ac.in'>Click here for results</a>",
    "1.4.1.5": """<ul><li>The library opens daily at sharply 9am everyday except for holidays sometimes and will close by 9pm.</li>
                <li>There will be all types of books available along with the newspaper daily.</li>
                <li>You need to enter the book details and your details if you want to bring the book to the hostelrooms.</li>
                </ul>""",
    "1.4.1.6":"""<b>SE project roadmap</b>:<ul><li>Define the scope of your software project.</li><li>
                Isolate tasks within the project.</li><li>
                Design time-based objectives</li><li>
                Delegate tasks to teams or individuals.</li><li>
                Establish schedules for your team</li><li>
                Perform appropriate risk assessments.</li><li>
                Gather and analyze project data.</li><li>
                Make adjustments to ensure success.</li></ul>""",
    "1.4.1.7" : """<ul><li>The students who are not from the eligible background need to pay the whole money to college.</li>
	<li>They don't get any scholarships.</li><li>The students who are eligible for scholarship need to pay the Vidyadevena,Vasathidevena money for every semester</li></ul>""",
    "1.4.1.8" : """<b>DSP Project roadmap:</b><br>
                1.Framing the Problem. Understanding and framing the problem is the first step of the data science <br>
                2.Collecting Data. The next step is to collect the right set of data.<br>
                3.Cleaning Data.<br>
                4.Exploratory Data Analysis (EDA)<br>
		5.Model Building and Deployment<br>
                6.Communicating Your Results. """
}                

e3_academics={
    "1.5.1.1":"""<b>Sem1 subjects</b>:<ul><li>Operating System(OS)</li><li>Computer Networks(CN)</li><li>Software Engineering(SE)</li><li>Mathematical Foundations for Data Science(MFDS)</li><li>Elective - I</li></ul>
<b>Sem2 subjects</b>:<ul><li>Cryptography and Networks Security(CNS)</li><li>Artificial Intelligence(AI)</li><li>Elective - II</li><li>Elective - III</li><li>Open Elective-I</li><li>Career Development Course(CDC)</li></ul>""",
    "1.5.1.2" : "<b>Sem1 faculty</b>:<br>Dr.B.Bhaskar rao<br>S.Sateesh Kumar<br>M.AnilKumar<br>CH.Satish Kumar<br>Gnaneswara Rao<br><b>Sem2 faculty</b>:<br>Dr.B.Bhaskar rao<br>N.Sesha Kumar<br>P.Ravi kumar<br>S.Sateesh Kumar<br>M.AnilKumar<br>CH.Satish Kumar",
    "1.5.1.3": "Mini Project:",
    "1.5.1.4":"<a href = 'https://examcell.rguktsklm.ac.in'>Click here for results</a>",
    "1.5.1.5": """<ul><li>The library opens daily at sharply 9am everyday except for holidays sometimes and will close by 9pm.</li>
                <li>There will be all types of books available along with the newspaper daily.</li>
                <li>You need to enter the book details and your details if you want to bring the book to the hostelrooms.</li>
                </ul>""",
    "1.5.1.6":"""<b>Summer Intern rules</b>:<br><ul><li>Students shall opt for summer internship to gain ample field knowledge in the 
                relevant field of engineering such that theoretical knowledge gained in the class can be applied to solve the practical field problem.
            </li><li>Students can take a challenging task, may be small portion, and apply the knowledge gained to solve it.
            </li><li>It is aimed at solving some of the problems of the society/ local region that have practical applications and benefit the society.
            </li><li>Students of RGUKT are permitted to undertake internships in RGUKT campuses also. 
            </li><li>Students shall devote SIX (06) weeks for summer internship in an organization.
            </li><li>Head of the department may depute faculty members for monitoring the student summer internship by communicating to the company guide. 
           </li><li>If a student is found “ABSENT” for the summer internship program during his/her scheduled course of time, then he/she must complete the summer internship within stipulated time suggested by the HoD/Dean (Academic)/Director.""",
    "1.5.1.7":"""<ul><li>The students who are not from the eligible background need to pay the whole money to college.</li>
	<li>They don't get any scholarships.</li><li>The students who are eligible for scholarship need to pay the Vidyadevena,Vasathidevena money for every semester</li></ul>"""
}

e4_academics={
    "1.6.1.1":"<b>Sem1 subjects</b>:<ul><li>Machine Learning</li><li>Elective-IV</li><li>Open Elective II</li></ul><b>Sem2 subjects</b>:<ul><li>Elective-V</li><li>Open Elective-III(Big Data Analytics)</li><li>Open Elective-IV</li><li>Community Service</li></ul>",
    "1.6.1.2" : "<b>Sem1 faculty</b>:<br>Mr. S.Sateesh Kumar<br>CH.Satish kumar<br><b>Sem2 faculty</b>:Mr. S.Sateesh Kumar<br>CH.Satish kumar",
    "1.6.1.3": """<b>Longterm Internship guidelines</b>:<br>Long-term internship (optional) is an opportunity through which students can experience a real-life engineering workplace and understand how their engineering and professional skills and knowledge can be utilized in Industry. 
                Minimun 6 months internship will be considered as long-term internship.Maximum allowed duration is One Year.""",
    "1.6.1.4":"<a href = 'https://examcell.rguktsklm.ac.in'>Click here for results</a>",
    "1.6.1.5": """<ul><li>The library opens daily at sharply 9am everyday except for holidays sometimes and will close by 9pm.</li>
                <li>There will be all types of books available along with the newspaper daily.</li>
                <li>You need to enter the book details and your details if you want to bring the book to the hostelrooms.</li>
                </ul>""",
    "1.6.1.6":"""<ul><li>The students who are not from the eligible background need to pay the whole money to college.</li>
	<li>They don't get any scholarships.</li><li>The students who are eligible for scholarship need to pay the Vidyadevena,Vasathidevena money for every semester</li></ul>"""
}

admission_dict = {
    '2.1.1': """Candidates who wish to apply for AP RGUTK Admission stream shall submit their AP IIIT Admission Online Application 2023 through online mode only at <a href = 'http://rgukt.in/'>rgukt site</a><br><br>
        The application process for AP RGUKT IIIT Admission 2023 is a simple and straightforward process.Candidates can follow the steps given below to apply for the program (AP IIIT Admission Application Form):
	<ul><li>Visit the official website of RGUKT (www.rgukt.in).
        </li><li>Click on the “Admissions” tab on the homepage.
        </li><li>Select the campus for which you want to apply.
        </li><li>Click on the “Apply Online” button.
        </li><li>Fill in the required details in the application form.
        </li><li>Upload the necessary documents and photographs.
        </li><li>Pay the application fee through the online mode.
        </li><li>Submit the application form.</li></ul<br><b>NOTE:</b><br>
            Please carry study certificates from 4th class to 10th class and soft copy of your passport size photograph to AP Online Center for filling the AP RGUKT Application.<br>
            The candidates who are applying for the AP RGUKT Admissions are advised to pay a fees of Rs.400 for OC candidates, Rs.250 for BC and Rs.150 for SC, ST candidates.<br>
            The detailed application process can be found <a href = 'https://teachersbadi.in/how-to-apply-for-ap-rgukt-iiit-admissions-in-6-year-integrated-btech-progra/'>here</a>""",
    '2.1.2':"""Before applying, candidates need to ensure that they meet the following eligibility criteria:<br>
            <ul><li>The candidate should have completed 10th class or equivalent from a recognized board with a minimum grade point average of 9.0 for general category students and 8.0 for reserved category students.
            </li><li>The candidate should have studied Mathematics, Physics, and Chemistry during their 10th standard or equivalent.
            </li><li>The candidate should be a citizen of India and must belong to Andhra Pradesh.</li></ul>""",
    '2.1.3':"""<b>Eligibility criteria</b><br><ul><li>IIIT Admission AP will be based on merit in the 10th class Grade Point Average (GPA) and Grade obtained in each subject, and by following the statutory reservations of the State.</li>
            <li>A deprivation score of 0.4 shall be added to the 10th class GPA of applicants from non-residential Government Schools including the ZP, Municipal, KV, AP Model Schools and KGBV Schools for selection, with an objective of providing weightage to help the students from socially, economically deprived sections of the society for admissions.</li></ul>""",
    '2.1.4':"""<a href = "http://admissions23.rgukt.in/ind/home">Check your admission result here!</a>"""
}
aspirant_other_dict = {
    '2.2.1' : """<ul><li>RGUKT is a fully residential environment.</li>
	<li>This is necessary because most of the rural students come from a geographically distributed wide area and would not be able to commute to the campus.
	</li><li>Thus, it is essential to provide a fully residential campus with all of the facilities included such as a shops, hospitals, bank, laundry, barbershops, etc. appropriate for a community of about 20,000 people consisting of 12,000 students, 3000 faculty and staff and 5000 service providers of various types.
	</li><li>students who are willing to study in RGUKT should stay in campus only, day-scholar facility is not available.	
</li><li>Internet will be provided at both hostels and class rooms.
	</li><li>Fine quality food is provided four times a day.
	</li><li>Library, yoga hall, Fine art departments helps students to have a stress free education.
	</li><li>Most importantly campus will have less pollution levels compared to cities and towns around.""",
    '2.2.2' : """<b>RGUKT Courses</b><p>The 6-Year Integrated Engineering course is divided in to the following two stages: </p>
		<b>Stage 1: Pre University Course (2 years)</b><ul><li>M.P.C group will be offered with the following courses:</li>
<li>Mathematics</li>
<li>Physics</li>
<li>Chemistry</li>
<li>English</li>
<li>Telugu / Sanskrit</li>
<li>Information Technology</li>
<li>Biology (Optional)</li>
</ul>
<b>Stage 2: B.Tech (4 years) </b><ul>
<li>Following branches will be offered: Chemical Engineering</li>
<li>Civil Engineering</li>
<li>Computer Science and Engineering</li>
<li>Electrical and Electronics Engineering</li>
<li>Electronics and Communications Engineering</li>
<li>Mechanical Engineering</li>
</ul>
""",
    '2.2.3' : """<ul><li>Hostels with fine facilities are available for both boys and girls seperately.</li>
<li>Beds and cots will be provided.</li>
<li>Four sets of Common washrooms are available for each floor</li>
<li>water timings are unpredictable sometimes</li>
<li>Rooms will be allocated to group of people of either 3 or 6</li></ul>""",
    '2.2.4' : """<ul><li>As a government sponsored university, the tuition fees at Rajiv Gandhi University are highly subsidized by the AP government.</li>
<li>The annual fee (for AP students) for the first two years (Pre University program) is Rs.45,000/- per annum + Mess Charges for PUC program and Rs.50,000/- per annum + Mess Charges for B.Tech program.</li>
<li>Fees of students under army reservation are not subsidized by the AP government, they have to pay the complete fee.""",
    '2.2.5' : """<ul><li>Students can leave the campus after PUC, if they are willing to join any other institute.</li>
<li>If any student wants to leave in between course, they have to pay the complete fee to leave the institute</li>
</ul>""",
    '2.2.6' : """<ul><li>Rajiv Gandhi University of Knowledge Technologies (RGUKT) IIIT is a renowned university in India that offers undergraduate programs in engineering and technology.</li>
            <li>It has three campuses in Andhra Pradesh, located in Srikakulam, Nuzvid, RK Valley, and Ongole.</li>
            <li>AP RGUKT IIIT is a prestigious university that offers integrated course of PUC(Pre-university course) + BTech in Computer Science and Engineering, Electronics and Communications Engineering, and other disciplines.</li></ul>"""
}


def get_chat_response(input):
    global flag
    if(input.lower() == 'start'):
        flag = 1
        reset_fun()
        return '<i>Choose a number from below</i><br><b>1</b>.Student<br><b>2</b>.Aspirant'
    elif(input in start.keys() and flag == 1):
        flag = 0
        return start_fun(input)
    elif(input in aspirant.keys() and start['2'] == 1):
        return aspirant_fun(input)
    elif(input in student.keys() and start['1'] == 1):
        return student_fun(input)
    elif(input in p1.keys() and student['1.1'] == 1):
        return p1_fun(input)
    elif(input in p2.keys() and student['1.2'] == 1):
        return p2_fun(input)
    elif(input in e1.keys() and student['1.3'] == 1):
        return e1_fun(input)
    elif(input in e2.keys() and student['1.4'] == 1):
        return e2_fun(input)
    elif(input in e3.keys() and student['1.5'] == 1):
        return e3_fun(input)
    elif(input in e4.keys() and student['1.6'] == 1):
        return e4_fun(input)
    elif(input in p1_academics.keys() and p1['1.1.1'] == 1):
        return p1_academics[input]
    elif(input in p2_academics.keys() and p2['1.2.1'] == 1):
        return p2_academics[input]
    elif(input in e1_academics.keys() and e1['1.3.1'] == 1):
        return e1_academics[input]
    elif(input in e2_academics.keys() and e2['1.4.1'] == 1):
        return e2_academics[input]
    elif(input in e3_academics.keys() and e3['1.5.1'] == 1):
        return e3_academics[input]
    elif(input in e4_academics.keys() and e4['1.6.1'] == 1):
        return e4_academics[input]
    elif(input in p1_others and p1['1.1.2'] == 1):
        return others[input[-1]]
    elif(input in p2_others and p2['1.2.2'] == 1):
        return others[input[-1]]
    elif(input in e1_others and e1['1.3.2'] == 1):
        return others[input[-1]]
    elif(input in e2_others and e2['1.4.2'] == 1):
        return others[input[-1]]
    elif(input in e3_others and e3['1.5.2'] == 1):
        return others[input[-1]]
    elif(input in e4_others and e4['1.6.2'] == 1):
        return others[input[-1]]
    elif(input in admission_dict.keys() and aspirant['2.1'] == 1):
        return admission_dict[input]
    elif(input in aspirant_other_dict.keys() and aspirant['2.2'] == 1):
        return aspirant_other_dict[input]
    else:
        return "Select valid option"

def reset_fun():
    start.update({}.fromkeys(start,0))
    aspirant.update({}.fromkeys(aspirant,0))
    student.update({}.fromkeys(student,0))
    p1.update({}.fromkeys(p1,0))
    p2.update({}.fromkeys(p2,0))
    e1.update({}.fromkeys(e1,0))
    e2.update({}.fromkeys(e2,0))
    e3.update({}.fromkeys(e3,0))
    e4.update({}.fromkeys(e4,0))

def student_fun(input):
    start['1'] = 0
    student[input] = 1
    if(input == '1.1'):
        return "<i>Choose a number from below</i><br><b>1.1.1</b>.Academics<br><b>1.1.2</b>.Others"
    elif(input == '1.2'):
        return "<i>Choose a number from below</i><br><b>1.2.1</b>.Academics<br><b>1.2.2</b>.Others"
    elif(input == '1.3'):
        return "<i>Choose a number from below</i><br><b>1.3.1</b>.Academics<br><b>1.3.2</b>.Others"
    elif(input == '1.4'):
        return "<i>Choose a number from below</i><br><b>1.4.1</b>.Academics<br><b>1.4.2</b>.Others"
    elif(input == '1.5'):
        return "<i>Choose a number from below</i><br><b>1.5.1</b>.Academics<br><b>1.5.2</b>.Others"
    elif(input == '1.6'):
        return "<i>Choose a number from below</i><br><b>1.6.1</b>.Academics<br><b>1.6.2</b>.Others"

def p1_fun(input):
    student['1.1'] = 0
    p1[input] = 1
    if(input == '1.1.1'):
        return "<i>Choose a number from below</i><br><b>1.1.1.1</b>.Subject detials<br><b>1.1.1.2</b>.Faculty contacts<br><b>1.1.1.3</b>.Exam results<br><b>1.1.1.4</b>.Library details<br><b>1.1.1.5</b>.Laboratories"
    elif(input == '1.1.2'):
        return "<i>Choose a number from below</i><br><b>1.1.2.1</b>.Sports and Games<br><b>1.1.2.2</b>.Extra curricular activities<br><b>1.1.2.3</b>.Mess menu and timings<br><b>1.1.2.4</b>.Feedback forms<br><b>1.1.2.5</b>.Rules and regulations<br><b>1.1.2.6</b>.Health and safety<br><b>1.1.2.7</b>.Leave and Outpass management"

def p2_fun(input):
    student['1.2'] = 0
    p2[input] = 1
    if(input == '1.2.1'):
        return "<i>Choose a number from below</i><br><b>1.2.1.1</b>.Subject detials<br><b>1.2.1.2</b>.Faculty contacts<br><b>1.2.1.3</b>.Exam results<br><b>1.2.1.4</b>.Library details<br><b>1.2.1.5</b>.Laboratories"
    elif(input == '1.2.2'):
        return "<i>Choose a number from below</i><br><b>1.2.2.1</b>.Sports and Games<br><b>1.2.2.2</b>.Extra curricular activities<br><b>1.2.2.3</b>.Mess menu and timings<br><b>1.2.2.4</b>.Feedback forms<br><b>1.2.2.5</b>.Rules and regulations<br><b>1.2.2.6</b>.Health and safety<br><b>1.2.2.7</b>.Leave and Outpass management"
def e1_fun(input):
    student['1.3'] = 0
    e1[input] = 1
    if(input == '1.3.1'):
        return "<i>Choose a number from below</i><br><b>1.3.1.1</b>.Subject detials<br><b>1.3.1.2</b>.Faculty contacts<br><b>1.3.1.3</b>.Exam results<br><b>1.3.1.4</b>.Library details<br><b>1.3.1.5</b>.Laboratories<br><b>1.3.1.6</b>About Fees"
    elif(input == '1.3.2'):
        return "<i>Choose a number from below</i><br><b>1.3.2.1</b>.Sports and Games<br><b>1.3.2.2</b>.Extra curricular activities<br><b>1.3.2.3</b>.Mess menu and timings<br><b>1.3.2.4</b>.Feedback forms<br><b>1.3.2.5</b>.Rules and regulations<br><b>1.3.2.6</b>.Health and safety<br><b>1.3.2.7</b>.Leave and Outpass management" 

def e2_fun(input):
    student['1.4'] = 0
    e2[input] = 1
    if(input == '1.4.1'):
        return "<i>Choose a number from below</i><br><b>1.4.1.1</b>.Subject detials<br><b>1.4.1.2</b>.Faculty contacts<br><b>1.4.1.3</b>.Exam results<br><b>1.4.1.4</b>.Library details<br><b>1.4.1.5</b>.Laboratories"
    elif(input == '1.4.2'):
        return "<i>Choose a number from below</i><br><b>1.4.2.1</b>.Sports and Games<br><b>1.4.2.2</b>.Extra curricular activities<br><b>1.4.2.3</b>.Mess menu and timings<br><b>1.4.2.4</b>.Feedback forms<br><b>1.4.2.5</b>.Rules and regulations<br><b>1.4.2.6</b>.Health and safety<br><b>1.4.2.7</b>.Leave and Outpass management" 

def e3_fun(input):
    student['1.5'] = 0
    e3[input] = 1
    if(input == '1.5.1'):
        return "<i>Choose a number from below</i><br><b>1.5.1.1</b>.Subject detials<br><b>1.5.1.2</b>.Faculty contacts<br><b>1.5.1.3</b>.Exam results<br><b>1.5.1.4</b>.Library details<br><b>1.5.1.5</b>.Laboratories"
    elif(input == '1.5.2'):
        return "<i>Choose a number from below</i><br><b>1.5.2.1</b>.Sports and Games<br><b>1.5.2.2</b>.Extra curricular activities<br><b>1.5.2.3</b>.Mess menu and timings<br><b>1.5.2.4</b>.Feedback forms<br><b>1.5.2.5</b>.Rules and regulations<br><b>1.5.2.6</b>.Health and safety<br><b>1.5.2.7</b>.Leave and Outpass management" 
def e4_fun(input):
    student['1.6'] = 0
    e4[input] = 1
    if(input == '1.6.1'):
        return "<i>Choose a number from below</i><br><b>1.6.1.1</b>.Subject detials<br><b>1.6.1.2</b>.Faculty contacts<br><b>1.6.1.3</b>.Exam results<br><b>1.6.1.4</b>.Library details<br><b>1.6.1.5</b>.Laboratories"
    elif(input == '1.6.2'):
        return "<i>Choose a number from below</i><br><b>1.6.2.1</b>.Sports and Games<br><b>1.6.2.2</b>.Extra curricular activities<br><b>1.6.2.3</b>.Mess menu and timings<br><b>1.6.2.4</b>.Feedback forms<br><b>1.6.2.5</b>.Rules and regulations<br><b>1.6.2.6</b>.Health and safety<br><b>1.6.2.7</b>.Leave and Outpass management" 
def start_fun(input):
    start[input] = 1
    if(input == '2'):
        return "<i>Choose a number from below</i><br><b>2.1</b>.Admissions<br><b>2.2</b>.Others"
    elif(input == '1'):
        return "<i>Choose a number from below</i><br><b>1.1</b>.P1<br><b>1.2</b>.P2<br><b>1.3</b>.E1<br><b>1.4</b>.E2<br><b>1.5</b>.E3<br><b>1.6</b>.E4"
    
def aspirant_fun(input):
    start['2'] = 0
    aspirant[input] = 1
    if(input == '2.1'):
        return "<i>Choose a number from below</i><br><b>2.1.1</b>.Admission process<br><b>2.1.2</b>.Eligibility<br><b>2.1.3</b>.Selection criteria<br><b>2.1.4</b>.Results"
    elif(input == '2.2'):
        return "<i>Choose a number from below</i><br><b>2.2.1</b>.College life<br><b>2.2.2</b>.Available courses<br><b>2.2.3</b>.Hostel life<br><b>2.2.4</b>.Fee details<br><b>2.2.5</b>.Academic details<br><b>2.2.6</b>.what is RGUKT"
    else:
        return "select valid option"

@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    response = get_chat_response(msg)
    return response

if __name__ == '__main__':
    app.run()