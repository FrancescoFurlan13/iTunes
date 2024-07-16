from database.DB_connect import DBConnect
from model.album import Album


class DAO():

    @staticmethod
    def getAlbumDurata(d):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT a.*, SUM(t.Milliseconds) as durata
                        FROM track t, album a 
                        WHERE a.AlbumId = t.AlbumId 
                        group by a.AlbumId 
                        having durata > %s
                        """
            cursor.execute(query, (d,))

            for row in cursor:
                result.append(Album(**row))
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def getEdges(idMap):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT DISTINCT t1.AlbumId AS a1, t2.AlbumId AS a2
                        FROM PlaylistTrack p1
                        JOIN Track t1 ON p1.TrackId = t1.TrackId
                        JOIN PlaylistTrack p2 ON p1.PlaylistId = p2.PlaylistId
                        JOIN Track t2 ON p2.TrackId = t2.TrackId
                        WHERE t1.AlbumId < t2.AlbumId;
                                """
            cursor.execute(query,)

            for row in cursor:
                if row['a1'] in idMap and row['a2'] in idMap:
                    result.append((idMap[row['a1']], idMap[row['a2']]))
            cursor.close()
            cnx.close()
        return result
