        sql_query = f"""
        SELECT 
            [AC_CLASS], [AC_MASS], [NUM_ENGS], [REMAINS_COLLECTED], [INCIDENT_MONTH],
            [INCIDENT_YEAR], [TIME_OF_DAY], [AIRPORT], [STATE], [HEIGHT], [SPEED], [PHASE_OF_FLT],
            [SPECIES], [BIRDS_SEEN], [BIRDS_STRUCK], [SIZE]
        FROM 
            [{table_name}]
        WHERE 
            [INCIDENT_YEAR] > 2005
        """