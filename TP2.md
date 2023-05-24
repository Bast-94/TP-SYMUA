---


---

<h1 id="tp-2-de-systèmes-multi-agents-sur-gama">TP 2 de Systèmes multi-agents sur GAMA</h1>
<h2 id="choix-du-modèle">Choix du modèle</h2>
<p>Pour ce travail pratique sur GAMA je vais travailler sur le modèle <em>Segregation</em></p>
<h2 id="présentation-du-modèle">Présentation du modèle</h2>
<h3 id="but-du-modèle">But du modèle</h3>
<p>Le modèle a pour but de simuler le comportement communautaire des êtres humains, à savoir le fait qu’un humain a une préférence à être proche de ceux de son groupe et loin des autres.</p>
<h3 id="environnement">Environnement</h3>
<p>L’environnement est une carte qui représente un quartier d’une ville vue du dessus. Le quartier est composé de bâtiments de tailles variables. Au niveau du code il correspond à une liste de <code>species</code> appelées <code>space</code>.  <code>space</code> correspond à un endroit habitable par un ou plusieurs agents ( <code>people</code>) selon la capacité (<code>capacity</code>) .</p>
<h4 id="variables-globales">Variables globales</h4>
<ul>
<li>Liste de places libres pour les <code>people</code></li>
<li>Liste de toutes les places</li>
<li>Le nombre de groupe</li>
<li>La densité d’individus</li>
<li>Le pourcentage désiré de souhaité <code>percent_similar_wanted</code></li>
<li>La distance de perception, la distance maximale à laquelle un <code>people</code> va percevoir les autres et définir s’il est satisfait ou non(<code>is_happy</code>).</li>
</ul>
<h3 id="agents">Agents</h3>
<p>Les agents sont ici les <code>people</code> ils se présentent sous la forme de cercles de couleurs.<br>
les <code>people</code> possèdent:</p>
<ul>
<li>Une liste de <code>people</code> qui correspond à ses voisins</li>
<li>Un habitat <code>current_building</code> de type <code>space</code> dans lequel il se trouve</li>
<li>Un état de joie <code>is_happy</code> de type booléen, il est calculé en fonction du voisinage (<code>total_nearby</code>) et  (<code>percent_similar_wanted</code>)<br>
Les <code>people</code> peuvent:</li>
<li>Changer de localisation avec <code>move_to_new_place</code></li>
<li>Avoir un <code>reflex</code>  <code>migrate</code> quand il ne sont pas satisfait de leur localisation actuelle , dans ce cas ils feront appel à <code>move_to_new_place</code></li>
</ul>
<h3 id="déroulement-du-modèle">Déroulement du modèle</h3>
<ul>
<li>Initialisation des <code>spaces</code></li>
<li>Initialisation des <code>people</code></li>
<li>Demande des <code>people</code> à bouger, il changeront de place par réflexe</li>
</ul>
<h2 id="expérimentation-variation-des-différents-paramètres">Expérimentation, variation des différents paramètres</h2>
<h3 id="avec-2-communautés">Avec 2 communautés</h3>
<p>Dans les études avec deux communautés on se concentrera sur l’influence de <code>percent_similar_wanted</code> sur la répartition des groupes dans la carte:</p>

<table>
<thead>
<tr>
<th><code>percent_similar_wanted</code></th>
<th>observations</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>0.05</td>
<td>On remarque que l’intégralité de la population est très rapidement joyeuse et la répartition des groupes est diversifiée</td>
<td></td>
</tr>
<tr>
<td>0.5</td>
<td>On remarque que l’intégralité de la population est moins rapidement joyeuse et des régions de la carte sont uniformément composée que d’un seul groupe</td>
<td></td>
</tr>
<tr>
<td>0.9</td>
<td>La quasi intégralité de la population n’est pas satisfaite, et la répartition des groupes est sans cesse diversifiée</td>
<td></td>
</tr>
</tbody>
</table><h3 id="avec-5-communautés">Avec 5 communautés</h3>
<p>Dans le cas d’une analyse avec 5 groupes existants et <code>percent_similar_wanted</code> mis à 50% nous avons une satisfaction totale qui est plus longue à arriver. Cela peut s’expliquer par le fait qu’un individu a plus de chance d’être entouré d’autres d’un groupe différent, donc à chaque itération il sera plus probable qu’une part des individus soient encore insatisfaits. En terme de répartition les 5 groupes se concentrent dans des régions bien délimitée.</p>
<h2 id="idées-à-ajouter-au-modèle">Idées à ajouter au modèle</h2>
<ul>
<li>Faire en sorte que chaque individu ait un <code>percent_similar_wanted</code>personnel, en y initialisant à chaque individu (<code>people</code>) un taux compris entre <span class="katex--inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>0</mn></mrow><annotation encoding="application/x-tex">0</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">0</span></span></span></span></span> et <span class="katex--inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>1</mn></mrow><annotation encoding="application/x-tex">1</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height: 0.64444em; vertical-align: 0em;"></span><span class="mord">1</span></span></span></span></span> ,</li>
<li>Pouvoir créer une stratégie de au sein de chaque communauté pour s’organiser sur les place à prendre ( implémentation ambitieuse)</li>
<li>Faire en sorte qu’un individu fasse une analyse sur la globalité de la carte pour trouver le meilleur endroit qui le satisfasse en fonction de son <code>percent_similar_wanted</code>.</li>
<li></li>
</ul>

