---
title: Grade Calculator
author:
- Vitor Inserrra
page: logistics
template: overview
---
# Grade Calculator

<script type="text/javascript" src="../../static/grade_calc/grade_calc.js"></script>
<script type="text/javascript">window.onload = set_abs</script>

<link rel="stylesheet" href="../../static/grade_calc/grade_calc.css"></link>

***Disclaimer: This is a Beta version of the grade calculator. It is to help you estimate your grade, but it does not guarantee you a certain grade.***

## Grades
<h4>Calculate grade as:</h4>
<button onclick="set_rel()" id="relative" class="grade-type-unselected" >Relative</button>
<button onclick="set_abs()" id="absolute" class="grade-type-selected">Absolute</button>
<p>*All grades out of 100</p>

<br />

<div class="grades">
<h4>Exercises (35%)</h4>
<label>Average for Exercises</label>
    <input type="number" id="ex-avg" class="avg" />
</div>
<div class="category">
<div class="columns">
<label>EX00</label>
    <input onchange="avg_1drop('ex0', 12)" type="number" id="ex00" class="input" />
</div>
<div class="columns">
<label>EX01</label>
    <input onchange="avg_1drop('ex0', 12)" type="number" id="ex01" class="input" />
</div>
<div class="columns">
<label>EX02</label>
    <input onchange="avg_1drop('ex0', 12)" type="number" id="ex02" class="input" />
</div>
<div class="columns">
<label>EX03</label>
    <input onchange="avg_1drop('ex0', 12)" type="number" id="ex03" class="input" />
</div>
<div class="columns">
<label>EX04</label>
    <input onchange="avg_1drop('ex0', 12)" type="number" id="ex04" class="input" />
</div>
<div class="columns">
<label>EX05</label>
    <input onchange="avg_1drop('ex0', 12)" type="number" id="ex05" class="input" />
</div>
<div class="columns">
<label>EX06</label>
    <input onchange="avg_1drop('ex0', 12)" type="number" id="ex06" class="input" />
</div>
<div class="columns">
<label>EX07</label>
    <input onchange="avg_1drop('ex0', 12)" type="number" id="ex07" class="input" />
</div>
<div class="columns">
<label>EX08</label>
    <input onchange="avg_1drop('ex0', 12)" type="number" id="ex08" class="input" />
</div>
<div class="columns">
<label>EX09</label>
    <input onchange="avg_1drop('ex0', 12)" type="number" id="ex09" class="input" />
</div>
<div class="columns">
<label>EX10</label>
    <input onchange="avg_1drop('ex0', 12)" type="number" id="ex10" class="input" />
</div>
<div class="columns">
<label>EX11</label>
    <input onchange="avg_1drop('ex0', 12)" type="number" id="ex11" class="input" />
</div>
</div>

<br />

<div class="grades">
<h4>Readings (5%)</h4>
<label>Average for Readings</label>
    <input type="number" id="rd-avg" class="avg"  />
</div>
<div class="category">
<div class="columns">
<label>RD00</label>
    <input onchange="avg_1drop('rd0', 3)" type="number" id="rd00" class="input" />
</div>
<div class="columns">
<label>RD01</label>
    <input onchange="avg_1drop('rd0', 3)" type="number" id="rd01" class="input" />
</div>
<div class="columns">
<label>RD02</label>
    <input onchange="avg_1drop('rd0', 3)" type="number" id="rd02" class="input" />
</div>
</div>

<br />

<div class="grades">
<h4>Async Lesson Responses on Gradescope (10%)</h4>
<label>Average for Lesson Responses</label>
    <input type="number" id="ls-avg" class="avg" />
</div>
<input onchange="ls_toggle()" id="ls-toggle" type="checkbox"> Show all Lesson Responses</button>

<div style="display: none" id="ls-sec" class="category">
<div class="columns">
<label>LS00</label>
    <input onchange="avg_2drops('ls0', 21)" type="number" id="ls00" class="input" />
</div>
<div class="columns">
<label>LS01</label>
    <input onchange="avg_2drops('ls0', 21)" type="number" id="ls01" class="input" />
</div>
<div class="columns">
<label>LS02</label>
    <input onchange="avg_2drops('ls0', 21)" type="number" id="ls02" class="input" />
</div>
<div class="columns">
<label>LS03</label>
    <input onchange="avg_2drops('ls0', 21)" type="number" id="ls03" class="input" />
</div>
<div class="columns">
<label>LS04</label>
    <input onchange="avg_2drops('ls0', 21)" type="number" id="ls04" class="input" />
</div>
<div class="columns">
<label>LS05</label>
    <input onchange="avg_2drops('ls0', 21)" type="number" id="ls05" class="input" />
</div>
<div class="columns">
<label>LS06</label>
    <input onchange="avg_2drops('ls0', 21)" type="number" id="ls06" class="input" />
</div>
<div class="columns">
<label>LS07</label>
    <input onchange="avg_2drops('ls0', 21)" type="number" id="ls07" class="input" />
</div>
<div class="columns">
<label>LS08</label>
    <input onchange="avg_2drops('ls0', 21)" type="number" id="ls08" class="input" />
</div>
<div class="columns">
<label>LS09</label>
    <input onchange="avg_2drops('ls0', 21)" type="number" id="ls09" class="input" />
</div>
<div class="columns">
<label>LS10</label>
    <input onchange="avg_2drops('ls0', 21)" type="number" id="ls10" class="input" />
</div>


<div class="columns">
<label>LS11</label>
    <input onchange="avg_2drops('ls0', 21)" type="number" id="ls11" class="input" />
</div>
<div class="columns">
<label>LS12</label>
    <input onchange="avg_2drops('ls0', 21)" type="number" id="ls12" class="input" />
</div>
<div class="columns">
<label>LS13</label>
    <input onchange="avg_2drops('ls0', 21)" type="number" id="ls13" class="input" />
</div>
<div class="columns">
<label>LS14</label>
    <input onchange="avg_2drops('ls0', 21)" type="number" id="ls14" class="input" />
</div>
<div class="columns">
<label>LS15</label>
    <input onchange="avg_2drops('ls0', 21)" type="number" id="ls15" class="input" />
</div>
<div class="columns">
<label>LS16</label>
    <input onchange="avg_2drops('ls0', 21)" type="number" id="ls16" class="input" />
</div>
<div class="columns">
<label>LS17</label>
    <input onchange="avg_2drops('ls0', 21)" type="number" id="ls17" class="input" />
</div>
<div class="columns">
<label>LS18</label>
    <input onchange="avg_2drops('ls0', 21)" type="number" id="ls18" class="input" />
</div>
<div class="columns">
<label>LS19</label>
    <input onchange="avg_2drops('ls0', 21)" type="number" id="ls19" class="input" />
</div>
<div class="columns">
<label>LS20</label>
    <input onchange="avg_2drops('ls0', 21)" type="number" id="ls20" class="input" />
</div>
</div>

<br />

<h4>Challenge Questions (10%)</h4>
<div class="grades">
<label>Average for Challenge Questions</label>
    <input type="number" id="cq-avg" class="avg" />
</div>
<div class="category">
<div class="columns">
<label>CQ00</label>
    <input onchange="avg_2drops('cq0', 8)" type="number" id="cq00" class="input" /> 
</div>
<div class="columns">
<label>CQ01</label>
    <input onchange="avg_2drops('cq0', 8)" type="number" id="cq01" class="input" />
</div>
<div class="columns">
<label>CQ02</label>
    <input onchange="avg_2drops('cq0', 8)" type="number" id="cq02" class="input" />
</div>
<div class="columns">
<label>CQ03</label>
    <input onchange="avg_2drops('cq0', 8)" type="number" id="cq03" class="input" />
</div>
<div class="columns">
<label>CQ04</label>
    <input onchange="avg_2drops('cq0', 8)" type="number" id="cq04" class="input" />
</div>
<div class="columns">
<label>CQ05</label>
    <input onchange="avg_2drops('cq0', 8)" type="number" id="cq05" class="input" />
</div>
<div class="columns">
<label>CQ06</label>
    <input onchange="avg_2drops('cq0', 8)" type="number" id="cq06" class="input" />
</div>
<div class="columns">
<label>CQ07</label>
    <input onchange="avg_2drops('cq0', 8)" type="number" id="cq07" class="input" />
</div>
</div>

<br />

<h4>Quizzes and Final (40%)</h4>
<div class="category">
<div class="columns">
<label>Quiz 01</label>
    <input id="qz01" type="number" class="input"  />
    <input id="qz01cb" type="checkbox" checked> Completed</input>
</div>
<div class="columns">
<label>Quiz 02</label>
    <input id="qz02" type="number" class="input"  />
    <input id="qz02cb" type="checkbox" checked> Completed</input>
</div>
<div class="columns">
<label>Quiz 03</label>
    <input id="qz03" type="number" class="input"  />
    <input id="qz03cb" type="checkbox" checked> Completed</input>
</div>
<div class="columns">
<label>Final</label>
    <input id="final" type="number" class="input"  />
</div>
</div>

<br />

<button class="calc-btn" onclick="calculate_grade()">Calculate</button>

<br />

<h4>Final grade</h4>
<div class="category">
<input id="final-grade" class="final-grade" readonly></input>
</div>
</div>