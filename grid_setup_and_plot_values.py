#Create wireframe for plots and graphs
#Plot values

fig = plt.figure(figsize=(15, 12))

#Add Argentina logo
ax1 = fig.add_axes([.225, .775, .15, .15])
team1_img = Image.open('/Users/kevingquinn/code/kevingquinn/complete-football-analytics/team_logos/argentina_logo.png')
ax1.imshow(team1_img)
ax1.axis('off')

#Add dashboard title, date, team names, score
ax2 = fig.add_axes([.5, .8, .3, .1])
ax2.text(.5, .8, 'World Cup Final\nDecember 18th, 2022', fontsize=12, ha='center', fontdict={'family': 'monospace'})
team_1_text = ax2.text(.47, .4, 'Argentina', fontsize=24, ha='right', fontdict={'family': 'monospace'})
team_1_text.set_bbox(dict(facecolor=ARGENTINA_COLOR, alpha=.5, edgecolor=ARGENTINA_COLOR, boxstyle='round'))
team_2_text = ax2.text(.53, .4, 'France', fontsize=24, ha='left', fontdict={'family': 'monospace'})
team_2_text.set_bbox(dict(facecolor=FRANCE_COLOR, alpha=.5, edgecolor=FRANCE_COLOR, boxstyle='round'))
ax2.text(.47, 0, '3', fontsize=20, ha='right', fontdict={'family': 'monospace', 'weight': 'bold'})
ax2.text(.5, 0, '-', fontsize=20, ha='center', fontdict={'family': 'monospace', 'weight': 'bold'})
ax2.text(.53, 0, '3', fontsize=20, ha='left', fontdict={'family': 'monospace', 'weight': 'bold'})
ax2.axis('off')

#Add France logo
ax3 = fig.add_axes([.925, .775, .15, .15])
team2_img = Image.open('/Users/kevingquinn/code/kevingquinn/complete-football-analytics/team_logos/france_logo.png')
ax3.imshow(team2_img)
ax3.axis('off')

#Plot Argentina Pass Network
ax4 = fig.add_axes([.15, .25, .3, .5])
create_passnetwork(team1, ax4)

#Plot Table
ax5 = fig.add_axes([.5, .2, .3, .5])
column_labels, table_vals = create_table(team1, team2)

table = ax5.table(
    cellText=table_vals,
    cellLoc='center',
    edges='vertical',
    bbox=[0, .5, 1, .45]
)

table.set_fontsize(14)

#Setting borders so that there are only 2 vertical lines between the columns of the table
for (i, j), cell in table.get_celld().items():
    if j == 0:
        table.get_celld()[(i, j)].visible_edges = 'R'
    elif j == 2:
        table.get_celld()[(i, j)].visible_edges = 'L'
    else:
        table.get_celld()[(i, j)].visible_edges = 'LR'

ax5.axis('off')
    

#Plot France Pass Network
ax6 = fig.add_axes([.85, .25, .3, .5])
create_passnetwork(team2, ax6)

#Plot Argentina Shotmap
ax7 = fig.add_axes([.2, .05, .2, .2])
create_shotmap(team1, ax7)
ax7.axis('off')

#Plot xG Flowchart
ax8 = fig.add_axes([.5, .05, .3, .2])
create_xg_flow_chart(df, ax8)

#Plot France Shotmap
ax9 = fig.add_axes([.9, .05, .2, .2])
create_shotmap(team2, ax9)
ax9.axis('off')