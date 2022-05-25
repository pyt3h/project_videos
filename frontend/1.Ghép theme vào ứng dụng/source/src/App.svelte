<script>
  import { Router, Route, Link } from "svelte-navigator";
  import Home from './pages/Home.svelte';
  import ProductDetail from './pages/ProductDetail.svelte';
  import OrderProduct from './pages/OrderProduct.svelte';
  import ThankYou from './pages/ThankYou.svelte';
</script>

<Router>
  <header>
    <div class="bg-primary">
      <div class="container">
        <nav class="navbar navbar-expand navbar-dark bg-primary p-0">
          <ul class="navbar-nav">
            <li class="nav-item">
              <Link class="nav-link active" to="/">Sản phẩm</Link>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#/">Liên hệ</a>
            </li>
          </ul>
        </nav>
      </div>
    </div>
  </header>
  <main>
    <Route path="/" component={Home}/>
    <Route path="/product-detail/:id" component={ProductDetail}/>
    <Route path="/order-product/:id" component={OrderProduct}/>
    <Route path="/thank-you" component={ThankYou}/>
  </main>
</Router>
