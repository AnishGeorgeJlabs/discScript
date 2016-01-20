select fk_sku, data.url, data.category, error.description, result_test.details
from result_test
  inner join data on result_test.fk_sku = data.sku
  inner join error on result_test.fk_error = error.id_error
where fk_run = 7;
