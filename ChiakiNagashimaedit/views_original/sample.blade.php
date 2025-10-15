@extends('layouts.app')



@section('content')
<div class="product-detail">
    <h1>{{ $product->name }}</h1>

    @if ($product->isAvailable())
    <p class="status text-green-600">在庫あり</p>

    @foreach ($product->images as $image)
    <div class="product-image">
        <img src="{{ asset('storage/' . $image->path) }}" alt="{{ $product->name }}">
    </div>

    @if ($loop->first)
    <p class="note text-sm text-gray-500">※メイン画像です</p>
    @endif
    @endforeach

    <form method="POST" action="{{ route('cart.add', $product->id) }}">
        @csrf

        <div class="form-group">
            <label for="quantity">数量</label>
            <input type="number" name="quantity" id="quantity" min="1" value="1">

            @error('quantity')
            <p class="text-red-500 text-sm mt-1">{{ $message }}</p>
            @enderror
        </div>

        <button type="submit" class="btn btn-primary">カートに追加</button>
    </form>
    @else
    <p class="status text-red-600">在庫なし</p>
    @endif
</div>
@endsection