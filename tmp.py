iql = """
FROM elpi2a 2020-04-11 2020-04-16
WHERE 
	sourceType = "I2A" 
    railgunDidDeliver = 1
GROUP BY grps in ("elpb_enable_ganesha_tst1", "elpb_enable_ganesha_tst2"), grps HAVING TERM() =~ "elpb_ganesha_query.*"
SELECT 
	count(), 
    DISTINCT(jobid) AS num_jobs,
    count() / DISTINCT(jobid) as emails_per_job,
    i2aApplied, 
    declineJobClicks, 
    unsubscribeClicks, 
    [i2aApplied] / [i2aApplied + unsubscribeClicks + declineJobClicks] as jspr, 
    [i2aApplied + unsubscribeClicks + declineJobClicks] / COUNT() as jsrr,
    [declineJobClicks] / [i2aApplied] as jsdr, 
    [unsubscribeClicks] / [i2aApplied] as jsur,
    [employerSentiment=~"POSITIVE|MAYBE"] as conversions,
    [employerSentiment=~"POSITIVE|MAYBE"] / count() as cvr  
"""

def tokenize_iql(iql):
    for char in ['[',']','(',')','+','']:

    x = iql.split()
