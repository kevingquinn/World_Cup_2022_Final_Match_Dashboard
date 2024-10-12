#Removing Penalty Shootout data as it skews results
df = df[df.period < 5]