<script>
  import {Link} from "svelte-navigator";
</script>
<div class="container mt-5 mb-5">
  <div class="row">
    <div class="col-6">
      <img alt="" class="product-detail-image" src="images/ACER_0001.jpeg" />
    </div>

    <div class="col-6 mt-5">
      <div class="product-detail-title">Acer 001</div>
      <br />
      <table class="table">
        <tbody>
          <tr>
            <td>Hãng sản xuất:</td>
            <td>Acer</td>
          </tr>
          <tr>
            <td>Giá bán:</td>
            <td><b>6.500.000 ₫</b></td>
          </tr>
        </tbody>
      </table>
      <br />
      <Link class="btn btn-secondary" to="/">Quay lại</Link>
      <Link class="btn btn-primary" to="/order-product/1">Mua hàng</Link>
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