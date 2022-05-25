<script>
  import {Link} from "svelte-navigator";
  import {BASE_URL} from "../config";
  export let id;
  let product = {};

  let url = BASE_URL + '/api/get-product-by-id/' + id;
  fetch(url).then(resp => resp.json()).then(result => product = result);
</script>
<div class="container mt-5 mb-5">
  <div class="row">
    <div class="col-6">
      <img alt="" class="product-detail-image" src={BASE_URL + product.image} />
    </div>

    <div class="col-6 mt-5">
      <div class="product-detail-title">{product.name}</div>
      <br />
      <table class="table">
        <tbody>
          <tr>
            <td>Hãng sản xuất:</td>
            <td>{product.brand_name}</td>
          </tr>
          <tr>
            <td>Giá bán:</td>
            <td><b>{product.price} ₫</b></td>
          </tr>
        </tbody>
      </table>
      <br />
      <Link class="btn btn-secondary" to="/">Quay lại</Link>
      <Link class="btn btn-primary" to={"/order-product/"+product.id}>Mua hàng</Link>
    </div>
  </div>
</div>

<style>
  .product-detail-title {
    font-size: 24px;
    font-weight: bold;
  }

  .product-detail-image {
    width: 100%;
  }
</style>