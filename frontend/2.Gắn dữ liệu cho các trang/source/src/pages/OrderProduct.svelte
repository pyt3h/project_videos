<script>
  import {navigate} from "svelte-navigator";
  import {BASE_URL} from "../config";
  export let id;
  let product = {};
  let qty = 1;
  let customer_name = '';
  let customer_phone = '';
  let customer_address = '';

  async function saveOrder(e) {
    e.preventDefault();
    let url = BASE_URL + '/api/save-order';
    let data = {
      product_id: id,
      qty: qty,
      customer_name: customer_name,
      customer_phone: customer_phone,
      customer_address: customer_address
    };
    data = JSON.stringify(data);
    let options = {
      method: 'POST',
      body:data,
      headers: {"Content-Type": "application/json"}
    };
    let resp = await fetch(url, options);
    if(resp.status != 200) {
      let result = await resp.json();
      console.log(result);
      alert('Lỗi:' + result.error);
    }else {
      navigate('/thank-you');
    }
  }
  let url = BASE_URL + '/api/get-product-by-id/' + id;
  fetch(url).then(resp => resp.json()).then(result => product = result);
</script>
<div class="container mt-5 mb-5">
  <form on:submit={saveOrder} method="POST" novalidate>
    <h4>Đặt mua hàng trực tuyến</h4>
    <table class="table table-form">
      <tbody>
        <tr>
          <th colspan="2">
            <h5>Thông tin sản phẩm</h5>
          </th>
        </tr>
        <tr>
          <th>Tên sản phẩm:</th>
          <td>{product.name}</td>
        </tr>
        <tr>
          <th>Đơn giá:</th>
          <td>{product.price} ₫</td>
        </tr>
        <tr>
          <th>Số lượng:</th>
          <td>
            <div style="width:50px">
              <input class="form-control" type="number" min="1"
                value={qty} on:change={e => qty=e.target.value}
              />
            </div>
          </td>
        </tr>
        <tr>
          <th colspan="2">
            <h5>Thông tin người mua hàng</h5>
          </th>
        </tr>
        <tr>
          <th>Họ và tên: </th>
          <td><input class="form-control" on:change={e => customer_name =e.target.value} /></td>
        </tr>
        <tr>
          <th>Số điện thoại:</th>
          <td><input class="form-control" on:change={e => customer_phone =e.target.value}/></td>
        </tr>
        <tr>
          <th>Địa chỉ:</th>
          <td><input class="form-control" on:change={e => customer_address =e.target.value}/></td>
        </tr>
      </tbody>
    </table>
    <button class="btn btn-primary">
      Đặt mua
    </button>
  </form>
</div>

<style>
  input {
    width: 100%;
  }
</style>
