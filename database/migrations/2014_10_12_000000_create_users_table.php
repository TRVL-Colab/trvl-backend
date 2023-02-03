<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;
use PhpParser\Node\NullableType;

return new class extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('users', function (Blueprint $table) {
            $table->id();
            $table->string('firstname')->nullable();
            $table->string('lastname')->nullable();
            $table->string('slug')->unique();
            $table->string('username')->unique();
            $table->string('gender')->nullable();
            $table->date('date_of_birth')->nullable();
            $table->string('picture')->nullable();
            $table->string('place_of_birth')->nullable();
            $table->string('phone')->nullable();
            $table->string('address')->nullable();
            $table->string('email')->unique();
            $table->boolean('verify')->default(0);
            $table->boolean('is_admin')->default(0);
            $table->enum('status', ['active','inactive'])->default('active');
            $table->string('password');
            $table->rememberToken();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('users');
    }
};