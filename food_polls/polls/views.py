from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import generic

from .models import Poll
from products.models import Product

from .forms import PollsDetailForm


class IndexView(generic.ListView):
    model = Product
    template_name = 'polls/index.html'
    context_object_name = 'latest_polls_list'

    def get_queryset(self):
        return Product.objects.filter().order_by('-created')


class PollsDetailView(generic.DetailView):
    model = Product
    template_name = 'polls/detail.html'
    form_class = PollsDetailForm

    # questionにQuestionの結果が渡される
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        form = self.form_class(self.kwargs)
        if form.is_valid():
            value = list(form.data.values())[0]
            print('value', value)

            # questions = Question.objects.filter(
            #     pk=value,
            #     pub_date__lte=timezone.now()
            # )

            # if not questions:
            #     raise Http404("Question does not exist")

            try:
                Product.objects.get(
                    pk=value,
                    # pub_date__lte=timezone.now()
                )
            except Product.DoesNotExist:
                raise Http404("Product does not exist")

        # return Question.objects.filter(pub_date__lte=timezone.now())
        return Product.objects.filter().order_by('-created')

    """A base view for displaying a single object."""
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        print('context', context)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        # detail_form = PollsDetailForm(kwargs)

        # if detail_form.is_valid():
        #     vote_form = PollsVoteForm(request.POST)
        #     question = get_object_or_404(Question, pk=kwargs['pk'])

        #     if vote_form.is_valid():
        #         try:
        #             selected_choice = question.choice_set.get(
        #                 pk=request.POST['choice']
        #             )
        #         except (KeyError, Choice.DoesNotExist):
        #             # request.POST['choice'] は KeyError を送出
        #             return render(request, 'polls/detail.html', {
        #                 'question': question,
        #                 'error_message': "You didn't select a choice.",
        #             })
        #         else:
        #             selected_choice.votes += 1
        #             selected_choice.save()

        #             return HttpResponseRedirect(
        #                 reverse('polls:results', args=(question.id,))
        #             )
        #     else:
        #         error_message = "choice is not in the correct format."
        #         return render(
        #             request,
        #             'polls/detail.html', {
        #                 'question': question,
        #                 'error_message': error_message
        #             }
        #         )
        # else:
        raise Http404("Product does not exist")
