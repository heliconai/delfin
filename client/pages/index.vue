<template>
  <div class="relative content-center items-center justify-center">
    <div class="hero-bg absolute top-0 w-full h-full bg-center">
      <span id="blackOverlay" class="w-full h-full absolute opacity-50 bg-black"></span>
    </div>
    <div
      class="relative py-20 px-10 content-center items-center justify-center justify-content-center"
    >
      <div class="items-center flex">
        <div class="w-full px-4 ml-auto mr-auto text-center">
          <div>
            <h1
              class="mt-10 text-white font-semibold md:text-5xl text-3xl"
            >Multi-Task Annotations Toolkit.</h1>
            <p
              class="mt-4 text-lg md:text-2xl text-gray-300"
            >Delfin provides a unified interface to manage and accelerate generation of labeled data.</p>
          </div>
        </div>
      </div>
    </div>
    <div class="sm:flex sm:justify-between px-5 sm:space-x-5 z-50">
      <div
        class="relative text-center flex flex-col min-w-0 break-words bg-white w-full mb-8 shadow-lg rounded-lg"
      >
        <div class="px-4 py-5 flex-auto">
          <div
            class="text-white p-3 text-center inline-flex items-center justify-center w-12 h-12 mb-5 shadow-lg rounded-full bg-bittersweet"
          >
            <i class="material-icons">settings_ethernet</i>
          </div>
          <h6 class="text-xl font-semibold">Extensible</h6>
          <p
            class="mt-2 mb-4 text-gray-600"
          >Quickly add new labels, annotation types and data modalities.</p>
        </div>
      </div>
      <div
        class="relative text-center flex flex-col min-w-0 break-words bg-white w-full mb-8 shadow-lg rounded-lg"
      >
        <div class="px-4 py-5 flex-auto">
          <div
            class="text-white p-3 text-center inline-flex items-center justify-center w-12 h-12 mb-5 shadow-lg rounded-full bg-olive-green"
          >
          <i class="material-icons">
settings_remote
</i>
          </div>
          <h6 class="text-xl font-semibold">Built for Semi Supervised Learning</h6>
          <p
            class="mt-2 mb-4 text-gray-600"
          >Delfin aims to provide a convenient interface for Machine Learning practitioners to embed active learning and semi-supervised learning approaches into their annotation workflow..</p>
        </div>
      </div>
      <div
        class="relative text-center flex flex-col min-w-0 break-words bg-white w-full mb-8 shadow-lg rounded-lg"
      >
        <div class="px-4 py-5 flex-auto">
          <div
            class="text-white p-3 text-center inline-flex items-center justify-center w-12 h-12 mb-5 shadow-lg rounded-full bg-xanadu"
          >
            <i class="material-icons">cloud_done</i>
          </div>
          <h6 class="text-xl font-semibold">Ready to Deploy</h6>
          <p
            class="mt-2 mb-4 text-gray-600"
          >Dockerized and ready to deploy on your favourite cloud or on prem servers.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {}
</script>

<style>
.hero-bg {
  background-color: #061826;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='318' height='318' viewBox='0 0 200 200'%3E%3Cg %3E%3Cpolygon fill='%23b34b4b' points='100 57.1 64 93.1 71.5 100.6 100 72.1'/%3E%3Cpolygon fill='%23d95b5b' points='100 57.1 100 72.1 128.6 100.6 136.1 93.1'/%3E%3Cpolygon fill='%23b34b4b' points='100 163.2 100 178.2 170.7 107.5 170.8 92.4'/%3E%3Cpolygon fill='%23d95b5b' points='100 163.2 29.2 92.5 29.2 107.5 100 178.2'/%3E%3Cpath fill='%23ff6b6b' d='M100 21.8L29.2 92.5l70.7 70.7l70.7-70.7L100 21.8z M100 127.9L64.6 92.5L100 57.1l35.4 35.4L100 127.9z'/%3E%3Cpolygon fill='%23838546' points='0 157.1 0 172.1 28.6 200.6 36.1 193.1'/%3E%3Cpolygon fill='%239fa255' points='70.7 200 70.8 192.4 63.2 200'/%3E%3Cpolygon fill='%23bbbe64' points='27.8 200 63.2 200 70.7 192.5 0 121.8 0 157.2 35.3 192.5'/%3E%3Cpolygon fill='%239fa255' points='200 157.1 164 193.1 171.5 200.6 200 172.1'/%3E%3Cpolygon fill='%23838546' points='136.7 200 129.2 192.5 129.2 200'/%3E%3Cpolygon fill='%23bbbe64' points='172.1 200 164.6 192.5 200 157.1 200 157.2 200 121.8 200 121.8 129.2 192.5 136.7 200'/%3E%3Cpolygon fill='%23838546' points='129.2 0 129.2 7.5 200 78.2 200 63.2 136.7 0'/%3E%3Cpolygon fill='%23bbbe64' points='200 27.8 200 27.9 172.1 0 136.7 0 200 63.2 200 63.2'/%3E%3Cpolygon fill='%239fa255' points='63.2 0 0 63.2 0 78.2 70.7 7.5 70.7 0'/%3E%3Cpolygon fill='%23bbbe64' points='0 63.2 63.2 0 27.8 0 0 27.8'/%3E%3C/g%3E%3C/svg%3E");
}
</style>
