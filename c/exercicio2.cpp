/*Um pol�tico quer dar uma festa para os principais contribuintes de sua
campanha eleitoral. Crie um programa que, para cada contribui��o, leia o valor e o tipo
do contribuinte: pessoa jur�dica ('J') ou pessoa f�sica ('F'). Ser�o convidados para a
festa os contribuintes que doaram mais que 150 mil (para pessoas jur�dicas) ou 30 mil
(para pessoas f�sicas). Seu programa deve calcular e imprimir o percentual de
contribuintes que ser�o convidados para a festa.
Assuma que o valor �X� para tipo de contribuinte encerra a entrada de dados.*/

#include <stdio.h>
#include <ctype.h>
#define N 10

/*
	Fiz tipo de retorno como inteiro para atualizar a quantidade de pessoas cadastradas de acordo com o retorno dessa fun��o
	Poderia tamb�m ter passado o par�metro [int pos] por refer�ncia para resolver isso, dessa forma seria poss�vel manter como void.

	Pos:
		-1 pessoa com tipo X inseriada, terminar execu��o
		0 pessoa com tipo inv�lido, n�o termina execu��o, mas tentar� ler outro sem incrementar a qtd de pessoas cadastradas
		1 pessoa cadastrada com sucesso
*/
int LeContribuinte(char vetPessoas[], float vetValores[], int pos){
	char tipoPessoa;
	float valorContrib;
		
	//gambiarra. olhar isso -> https://stackoverflow.com/questions/9562218/c-multiple-scanfs-when-i-enter-in-a-value-for-one-scanf-it-skips-the-second-s
	if(pos != 0){
		getchar();
	}
	printf("Informe o tipo de pessoa \n");
	scanf("%c", &tipoPessoa);
	tipoPessoa = toupper(tipoPessoa);

	if((tipoPessoa == 'F') || (tipoPessoa == 'J')){
		vetPessoas[pos] = tipoPessoa;
	}else if(tipoPessoa == 'X'){
		return -1;
	}else{
		printf("Tipo de pessoa invalido\n");
		return 0;
	}

	printf ("Digite o valor da contribuicao \n");
	scanf("%f", &valorContrib);
	vetValores[pos] = valorContrib;
	return 1;
}

void CalculaPercentualContribuinte (char vetPessoas[],float vetValores[], int qtdPessoasCadastradas){
	
	float percentualContribuintes = 0;
	int i, qtdConvidados = 0;
	
	for(i=0; i < qtdPessoasCadastradas; i++){
		if(vetPessoas[i] == 'F' && vetValores[i] > 30000){
			qtdConvidados += 1;
		}else if(vetPessoas[i] == 'J' && vetValores[i] > 150000){
			qtdConvidados += 1;
		}
	}

	printf("Porcentagem de pessoas convidados: %f %%", qtdConvidados * 100 / (float)qtdPessoasCadastradas);
}

int main(){
	int qtdPessoasCadastradas = 0, foiCadastrado;
	char vetPessoas[N], terminou = 'F';
	float vetValores[N];
	while (qtdPessoasCadastradas < N && terminou == 'F'){
		foiCadastrado = LeContribuinte(vetPessoas, vetValores, qtdPessoasCadastradas);
		if(foiCadastrado == 1){
			qtdPessoasCadastradas += 1;
		}
		if(foiCadastrado == -1){
			terminou = 'T';
		}
	}
	CalculaPercentualContribuinte(vetPessoas, vetValores, qtdPessoasCadastradas);

	return (0);	
}
