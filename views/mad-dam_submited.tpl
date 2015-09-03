% rebase('base.tpl', title='Upload completed')
% if success:
<h1>Bravo !</h1>
<p>Vous avez aidé mad-dam à faire son coup !<p>
% else:
<h1>Zut mad-dam à raté son coup...</h1>
<p>Les champs titre et file sont requis dans le formulaire.
Seules les images sont acceptés.</p>
% end

