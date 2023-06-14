from .baseModel import BaseModel

class FilmModel(BaseModel):

  def GetAllFilms():
    sql = "SELECT film_id, title, release_year, language_id, special_features \
          FROM `film` \
          Order by film_id desc limit 3"
    return ( list(BaseModel.ExecuteQuery( sql)))
  
  def AddOneFilm():
    sql = "INSERT INTO `film` (`title`, `description`, `release_year`, `language_id`, `original_language_id`, \
           `rental_duration`, `rental_rate`, `length`, `replacement_cost`, `rating`, `special_features`, `last_update`) \
            VALUES ('pruebas01', NULL, NULL, '1', NULL, '3', '4.99', NULL, '19.99', 'G', NULL, CURRENT_TIMESTAMP)"
    return ( list(BaseModel.Execute( sql)))
  
  def DeleteOneFilm():
    sql = "delete from film where film_id = 1009"
    return ( list(BaseModel.Execute( sql)))