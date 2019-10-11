html_content = """<!DOCTYPE html>
<html>
<head>

<style>

*{
	margin: 0;
	padding: 0;
}
body {
	width: 100vw;
}
.univ {
	display: flex;
	flex-direction: column;
	align-items: center;
	flex-wrap: wrap;
	position: absolute;
	height: 1200px;
}

.top {
	width: 100%;
	background: #293B52;
	height: 60px;
	position: absolute;
	display: flex;
	align-items: center;
	justify-content: center;
}
.topcont {
	width: 95%;
	height: 70%;
	position: relative;
	display: flex;
	justify-content: space-between;
	align-items: center;
}
.sub {
	position: relative;
	height: 26px;

	font-family: Roboto;
	font-style: normal;
	font-weight: normal;
	font-size: 22px;
	line-height: 26px;
	color: #FFFFFF;
}
.but {
	position: relative;
height: 19px;
font-family: Roboto;
font-style: normal;
font-weight: normal;
font-size: 16px;
line-height: 19px;
color: #FFFFFF;
}
.post {
	width: 100%;
	position: absolute;
height: 108px;
top: 60px;
display: flex;
justify-content: center;
background: #F8D16C;
align-items: center;
}
.postcont {
	width: 95%;
	height: 70%;
	display: flex;
	align-items: center;
}
.postby, .poston {
	position: relative;
	height: 22px;
font-family: Roboto;
font-style: normal;
font-weight: normal;
font-size: 18px;
line-height: 21px;
color: #293B52;
margin-top: 10px;
margin-bottom: 10px;
}
.bodyc {width:100%;height: auto;}
.bodyt {
	position: relative;
	top: 200px;
	width: 95%;
	height: auto;
	display: flex;
	align-items: center;
	justify-content: center;
	flex-wrap: wrap;
	height: auto;
}
.bcontent {
	width: 80%;
	position: relative;
	height: auto;
font-family: Roboto;
font-style: normal;
font-weight: normal;
font-size: 16px;
line-height: 19px;

color: #000000;
}

.bottom {
	position: absolute;
width: 100%;
height: 156px;
top: 955px;
display: flex;
align-items: center;
background: #293B52;
justify-content: center;
}
.botcont {
	position: relative;
	width: 95%;
	display: flex;
	align-items: center;
	justify-content: space-between;
}
.botcont2 {
	position: relative;
	width: 30%;
font-family: Roboto;
font-style: normal;
font-weight: normal;
font-size: 1.125em;
line-height: 21px;
color: #FFFFFF;
}
.email, .phone, .follow {
	margin-top: 10px;
	margin-bottom: 10px;
}
.logo {
	position: relative;
width: 10%;
height: 10%;
}
.logo img {
	width: 100px;
	height: 100px;
}


</style>

<title> </title>
</head>

<body>
<div class="univ">
<div class='top'>
	<div class='topcont'>
		<div class='sub'>Schedule for End Term Examination</div>
		<div class='but'>Open in Channel I Noticeboard</div>
	</div>
</div>

<div class='post'>
	<div class='postcont'>
		<div class='postcont2'>
			<div class='postby'>Posted By:</div>
			<div class='poston'>Posted On:</div>
		</div>
	</div>
</div>
<div class='bodyc'>
<div class='bodyt'>
	<div class="bcontent">Greetings from HDFC Bank!<br><br> We are pleased to announce that HDFC Bank would be hosting the 3rd edition of its "Digital Innovation Summit" on 31 Oct - 1 Nov '18.<br><br> Digital Innovation Summit is a platform to connect with Early age startups from institutes / Fintech start-ups and companies for innovative solutions in BFSI space where Bank invites applications for latest solutions in BFSI space from the participants. The short listed applicants would be presenting their solutions to a panel comprising of HDFC Group Top Management & finalists will get an opportunity to develop their solutions for HDFC Bank.<br><br> So send in your entries today and do spread the word in your network to help your other start-up buddies connect with us.<br><br> Event details and application process are detailed below.<br><br> About the Event<br><br> Digital Innovation Summit is an annual event hosted by HDFC Bank with the objective to embrace the wave of disruptive innovation in the Fintech space in the country. It is created to be a platform to nurture the spirit of innovation and enterprise as part of the Banks strategic focus on customer convenience, access and delight, using technology as an enabler. The engagement with startups / technology driven institutions gives the Bank access to the latest offerings & products.<br><br> As a part of this engagement, Bank invites entries from Early age startups from institutes / Fintech startups / companies in various banking areas such as Branch automation, Payments, Customer service & experience, Mobile Banking, Social Banking, Analytics, Cloud Solutions, Cyber Security, Marketing & Communications,Operational Efficiency , New Age Technology like AR/VR, Blockchain, Artificial Intelligence etc from startups / Fintech companies. The Fintech companies / Startups are short-listed after pre-screening, and the finalists are given an opportunity to showcase a demo of their solutions to a panel of top management from HDFC Bank on the summit day. The winners get an opportunity to develop their solution for the Bank.<br><br> How to apply?<br><br> 1. Visit our web page www.hdfcbank.com/dis2018 <br><br>2. Go to Register & open the Application form <br><br>3. Fill the application form and submit your entry <br><br>Short-listed participants will be intimated by the Bank through email. So hurry up and send your applications! Registrations close on 5 Oct'18.</div>
</div>
</div>

<div class='bottom'>
	<div class='botcont'>
	<div class='botcont2'>
		<div class='email'>Email: img@iitr.ac.in</div>
		<div class='phone'>Phone: 01332-284521</div>
		<div class='follow'>Follow us on: Facebook Medium Instagram</div>
	</div>
        <div class='logo'><img style='display:block; width:100px;height:100px;' id='base64image' src='data:image/jpeg;base64, PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMjggMTI4Ij48ZGVmcz48c3R5bGU+LmF7ZmlsbDojMjkzYjUyO308L3N0eWxlPjwvZGVmcz48dGl0bGU+aW1nX2xvZ288L3RpdGxlPjxwYXRoIGNsYXNzPSJhIiBkPSJNMTAyLjk5MjksNDkuODIyN0g4Ny4wMDg5YTkuNzUxNiw5Ljc1MTYsMCwwLDAtMTkuNDEyNi0uMDk4OGwtLjAwOTQuMDk4OEg1MS41NDc5YTkuNzgxNiw5Ljc4MTYsMCwwLDAtOS42MDY0LTguODYzNSw4LjUzMjksOC41MzI5LDAsMCwwLTIuNDU0My4yODQ0LDkuNjk5LDkuNjk5LDAsMCwwLTIuMjI4Ljg1NjgsOS44NSw5Ljg1LDAsMCwwLTMuNDc0NCwzLjExNCw5LjczOTQsOS43Mzk0LDAsMCwwLTEuNjU4OSw0LjYwODNIMTYuMTQzNmEyNS4zNTY1LDI1LjM1NjUsMCwwLDEsMy43MzItMTIuNDY4MywyNS45ODQxLDI1Ljk4NDEsMCwwLDEsOS4zNzE0LTkuMDU1MUEyNS42OTYsMjUuNjk2LDAsMCwxLDQxLjgzNjksMjVoLjA3NDRhMjUuNjU3NiwyNS42NTc2LDAsMCwxLDE3LjA2MzksNi41NDc5bC41OTIyLjUzLjU5MjItLjUzYTI1LjcwNTcsMjUuNzA1NywwLDAsMSw0Mi44MzMzLDE4LjI3NDhaIi8+PHBhdGggY2xhc3M9ImEiIGQ9Ik0zMi4xMjA2LDI1bC0uMzMuMTI3N0EyNy42NCwyNy42NCwwLDAsMCwxNi4yNTUzLDQwLjY2MzFsLS4xMjc2LjMzVjI1WiIvPjxwYXRoIGNsYXNzPSJhIiBkPSJNMTExLjg3MjMsNzcuMzA1QTI1Ljc0MTYsMjUuNzQxNiwwLDAsMSw4Ny4wNSwxMDNWODcuMDE2QTkuNzUyOCw5Ljc1MjgsMCwwLDAsOTQuMTc3NSw3MS43NXEtLjEwMzgtLjE0OTEtLjIxMy0uMjk0M2wtLjUzMTktLjcwOTItLjcwOTIuNTMxOUEyNS43MTUyLDI1LjcxNTIsMCwwLDEsNTEuNjA0Niw1MS41OTU3SDY3LjU4NTFhOS43NTI5LDkuNzUyOSwwLDAsMCwxOS40MjM4LDBoMTUuOTg0YTI1LjgyNjgsMjUuODI2OCwwLDAsMS0uNjc5MSw1LjA2NTdsLS4xMjU5LjUzMzYuNDIyLjM1MTFBMjUuNjUyNCwyNS42NTI0LDAsMCwxLDExMS44NzIzLDc3LjMwNVoiLz48L3N2Zz4= ' /></div>
	</div>
</div>


</div>
</body>
</html>


"""
