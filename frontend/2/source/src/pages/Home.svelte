<script>
  import {Link} from "svelte-navigator";
  import {BASE_URL} from "../config";
  let productList = [];
  let total = 0;

  function getProductList() {
    let url = BASE_URL + '/api/search-product';
    fetch(url).then(resp => resp.json()).then(result => {
      productList = result.items;
      total = result.total;
      //console.log('productList=', productList);
    });
  }

  getProductList();
  
</script>

<div class="container mt-5 mb-5">
  <div class="row">
    <div class="col-3 p-3 card">
      <form>
        <div class="product-search-info mt-3">
          <label for="name" class="mb-1"><b>Tên sản phẩm:</b></label>
          <input name="name" class="form-control" placeholder="Nhập tên sản phẩm để tìm" />
        </div>

        <div class="brand-search-info mt-3">
          <label for="brandId"><b>Hãng sản xuất:</b></label>
          <div class="mt-2">
            <input type="radio" name="brandId" checked value="" />
            <span>Tất cả</span>
          </div>
          <div class="mt-1">
            <input name="brandId" type="radio" value="1" />
            <span>Acer</span>
          </div>
          <div class="mt-1">
            <input name="brandId" type="radio" value="2" />
            <span>Asus</span>
          </div>
          <div class="mt-1">
            <input name="brandId" type="radio" value="3" />
            <span>Lenovo</span>
          </div>
        </div>

        <div class="price-search-info mt-3">
          <label for="priceRange"><b>Mức giá:</b></label>
          <div class="mt-2">
            <input type="radio" name="priceRange" checked value="" />
            <span>Tất cả</span>
          </div>

          <div class="mt-1">
            <input type="radio" name="priceRange" value="1" />
            <span>Dưới 10 triệu</span>
          </div>

          <div class="mt-1">
            <input type="radio" name="priceRange" value="2" />
            <span>Từ 10-20 triệu</span>
          </div>

          <div class="mt-1">
            <input type="radio" name="priceRange" value="3" />
            <span>Trên 20 triệu</span>
          </div>
        </div>

        <button type="submit" class="btn btn-primary mt-4 mb-4">Tìm kiếm</button>
      </form>
    </div>
    <div class="col-9">
      <ul class="list-unstyled row">
        {#each productList as product}
          <li class="list-item col-sm-4 mt-3">
            <div class="item-container">
              <Link to={"product-detail/" + product.id} class="product-item">
                <img src={BASE_URL + product.image} class="product-image" alt="" />
                <div class="item-info">
                  <div>
                    <span class="product-name">{product.name}</span>
                  </div>
                  <div>
                    <span class="price-title">Giá bán :</span>
                    <span class="price">{product.price} ₫</span>
                  </div>
                </div>
              </Link>
            </div>
          </li>
        {/each}
      </ul>
      <nav aria-label="Page navigation example">
        <ul class="pagination">
          <li class="page-item"><a class="page-link" href="#/">&laquo;</a></li>
          <li class="page-item"><a class="page-link" href="#/">&lsaquo;</a></li>
          <li class="page-item"><a class="page-link" href="#/">&rsaquo;</a></li>
          <li class="page-item"><a class="page-link" href="#/">&raquo;</a></li>
        </ul>
        <span>Hiển thị 1-10 trên tổng số 25 sản phẩm</span>
      </nav>
    </div>
  </div>
</div>

<style>
  .product-image {
    width: 95%;
  }

  .price-title {
    font-style: italic;
    font-size: 14px;
  }

  .price {
    font-size: 16px;
    font-weight: bold;
  }

  .product-item,
  .product-item:link,
  .product-item:hover,
  .product-item:visited {
    text-decoration: none;
    color: black;
  }

  .item-container {
    position: relative;
    height: 100%;
    padding-bottom: 50px;
  }

  .item-info {
    position: absolute;
    bottom: 0px;
    height: 50px;
  }
</style>