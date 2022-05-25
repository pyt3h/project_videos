<script>
  import {Link} from "svelte-navigator";
  import {BASE_URL} from "../config";

  let loading = false;
  let brandList = [];
  let priceRangeList = [
    {minPrice: null, maxPrice: null, name: 'Tất cả'},
    {minPrice: 0, maxPrice: 10000000, name: 'Dưới 10 triệu'},
    {minPrice: 10000000, maxPrice: 20000000, name: 'Từ 10-20 triệu'},
    {minPrice: 20000000, maxPrice: null, name: 'Trên 20 triệu'},
  ];
  let productList = [];
  let total = 0;

  let searchParams = {
    keyword: '',
    brandId: null,
    priceRangeIndex: 0
  };

  function getProductList() {
    loading = true; //start get data
    let url = BASE_URL + '/api/search-product?';
    
    if(searchParams.keyword) url += `&keyword=${searchParams.keyword}`;
    if(searchParams.brandId) url += `&brand_id=${searchParams.brandId}`;

    let minPrice = priceRangeList[searchParams.priceRangeIndex].minPrice;
    let maxPrice = priceRangeList[searchParams.priceRangeIndex].maxPrice;

    if(minPrice) url += `&min_price=${minPrice}`;
    if(maxPrice) url += `&max_price=${maxPrice}`;

    fetch(url).then(resp => resp.json()).then(result => {
      productList = result.items;
      total = result.total;
      loading = false; //done
      //console.log('productList=', productList);
    });
  }

  function getBrandList() {
    let url = BASE_URL + '/api/get-all-brand';
    fetch(url).then(resp => resp.json()).then(result => {
      brandList = result;
      //console.log('brandList=', brandList);
    });
  }

  function searchProduct(e){
    e.preventDefault();
    getProductList();
  }

  getBrandList();
  getProductList();
  
</script>

<div class="container mt-5 mb-5">
  <div class="row">
    <div class="col-3 p-3 card">
      <form on:submit={searchProduct}>
        <div class="product-search-info mt-3">
          <label for="name" class="mb-1"><b>Tên sản phẩm:</b></label>
          <input name="name" class="form-control" placeholder="Nhập tên sản phẩm để tìm"
            bind:value={searchParams.keyword}
            on:click={e => searchParams.keyword = e.target.value}
          />
        </div>

        <div class="brand-search-info mt-3">
          <label for="brandId"><b>Hãng sản xuất:</b></label>
          <div class="mt-2">
            <input type="radio" name="brandId" 
              checked={!searchParams.brandId} 
              on:click={() => searchParams.brandId = null}
            />
            <span>Tất cả</span>
          </div>
          {#each brandList as brand}
            <div class="mt-1">
              <input name="brandId" type="radio" 
                checked={searchParams.brandId == brand.id}
                on:click={e => searchParams.brandId = brand.id}
              />
              <span>{brand.name}</span>
            </div>
          {/each}
        </div>

        <div class="price-search-info mt-3">
          <label for="priceRange"><b>Mức giá:</b></label>
          {#each priceRangeList as priceRange, index}
            <div class="mt-2">
              <input type="radio" name="priceRange" 
                checked={searchParams.priceRangeIndex == index}
                on:click={() => searchParams.priceRangeIndex = index}
              />
              <span>{priceRange.name}</span>
            </div>
          {/each}
        </div>

        <button type="submit" class="btn btn-primary mt-4 mb-4">Tìm kiếm</button>
      </form>
    </div>
    <div class="col-9">
      <ul class="list-unstyled row">
        {#if !loading && productList.length == 0}
          <div>Không tìm thấy sản phẩm nào</div>
        {/if}
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